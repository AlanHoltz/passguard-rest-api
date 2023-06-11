from app.models.box import BoxModel
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from app.utils.general import payload_has_fields
from app.utils.validators import is_valid_box


model = BoxModel()
box = Blueprint("box", __name__)



@box.route("/",methods=["GET","POST"])
@jwt_required()
def index():

    user_payload = get_jwt_identity()
    user_id = user_payload["user_id"]

    if request.method == "GET":
        return model.get_boxes_by_user_id(user_id)
    
    else:
        body = request.get_json()
        required_fields = ["name"]

        if payload_has_fields(body,required_fields) and is_valid_box(body):
            
            if not model.create_box(user_id,body["name"]) == "duplicated":
                return jsonify({"msg": f"box {body['name']} created successfully"})
            else:
                return jsonify({"error": f"box with name {body['name']} already exists"})
        
        else:
            return jsonify({"error": {
            "name": "Must be a string between 2 and 30 characters"
        }}) 



@box.route("/<string:box_name>", methods=["DELETE"])
@jwt_required()
def delete_box(box_name):
    user_id = get_jwt_identity()["user_id"]

    if not model.get_box_by_user_id_and_name(user_id,box_name):
        return jsonify({"error": f"There is no box with name {box_name} for the current user"})
    
    else:
        model.delete_box(user_id,box_name)
        return jsonify({"msg": f"box {box_name} successfully deleted"})
    