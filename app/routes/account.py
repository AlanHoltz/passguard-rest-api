from app.models.account import AccountModel
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from app.utils.general import payload_has_fields
from app.utils.validators import is_valid_account


model = AccountModel()
account = Blueprint("account", __name__)



@account.route("/",methods=["GET","POST"])
@jwt_required()
def index(box_name):

    user = get_jwt_identity()

    if request.method == "GET":
        return model.get_accounts_by_box_owner_and_box_name(user["user_id"], box_name)
    else:
        body = request.get_json()
        required_fields = ("description","user","password")
        
        if payload_has_fields(body,required_fields) and is_valid_account(body):

            model.create_account(user["user_id"],box_name,body)
            return jsonify({"msg": f"account {body['description']} created successfully"})

        else:
            return jsonify({"error": {
                "description": "Must be a string between 2 and 30 characters",
                "user": "Must be a string between 1 and 256 characters",
                "password": "Must be a string between 1 and 256 characters"
            }})


@account.route("/<int:account_id>", methods=["DELETE"])
@jwt_required()
def delete_account(box_name,account_id):
    box_owner = get_jwt_identity()["user_id"]

    if not model.get_account(box_owner,box_name,account_id):
        return jsonify({"error": f"There is no account with ID: {account_id} for the current box of the user"})
    
    else:
        model.delete_account(box_owner,box_name,account_id)
        return jsonify({"msg": f"account {account_id} successfully deleted"})