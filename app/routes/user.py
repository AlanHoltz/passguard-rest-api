from app.models.user import UserModel
from flask import request, jsonify, Blueprint
from os import getenv
from flask_jwt_extended import create_access_token
from app.utils.general import get_timestamp, payload_has_fields, is_correct_password ,sha256
from app.utils.validators import is_valid_user


model = UserModel()
user = Blueprint("user", __name__)


@user.route("/register", methods=["POST"])
def register():

    body = request.get_json()
    required_fields = ("username", "password")

    if payload_has_fields(body, required_fields) and is_valid_user(body):

        user_data = {
            "username": body["username"],
            "password": sha256(body["password"]),
        }


        if not model.register_user(user_data) == "duplicated":
            return jsonify({"msg": f'user {body["username"]} successfully registered'})

        else:
            return jsonify({"error": f'user {body["username"]} already registered'})

    else:
        return jsonify({"error": {
            "username": "Must be a string between 4 and 35 characters",
            "password": "Must be a sting between 8 and 64 characters, at least one uppercase, one lowercase and one number"
        }}) , 400


@user.route("/login", methods=["POST"])
def login():

    body = request.get_json()
    required_fields = ("username", "password")

    if payload_has_fields(body, required_fields):

        user = model.get_user_by_username(body["username"])

        if user and is_correct_password(user["user_password"], body["password"]):

            payload = dict(user)
            del payload["user_password"]
            payload["user_signup"] = get_timestamp(payload["user_signup"])
            
            token = create_access_token(identity=payload)
            return jsonify({"msg": token})

        else:
            return jsonify({"error": "user credentials are incorrect"}), 401

    else:
        return jsonify({"error": "You must include username and password on request body"}) , 400
