from app.utils.general import is_valid_string
import re


def is_valid_user(user_data):
    
    valid_username = is_valid_string(user_data["username"],4,35)
    
    password_regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,64}$"
    valid_password = is_valid_string(user_data["password"],8,64) and not re.match(password_regex,user_data["password"]) == None

    return valid_username and valid_password



def is_valid_box(box_data):

    valid_name = is_valid_string(box_data["name"],2,30)

    return valid_name



def is_valid_account(account_data):
    
    valid_description = is_valid_string(account_data["description"],2,30)
    valid_user = is_valid_string(account_data["user"],1,256)
    valid_password = is_valid_string(account_data["password"],1,256)

    return valid_description and valid_user and valid_password