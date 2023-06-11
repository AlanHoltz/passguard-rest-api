import hashlib
import uuid
from os import getenv

def sha256(password):
    salt = uuid.uuid4().hex
    hashed_pw = hashlib.sha256(salt.encode(
        "utf-8") + password.encode("utf-8")).hexdigest()
    return f'{hashed_pw}:{salt}'



def is_correct_password(hash, password):
    
    hashed_pw, salt = hash.split(":")

    return hashed_pw == hashlib.sha256(salt.encode("utf-8") + password.encode("utf-8")).hexdigest()



def get_timestamp(mysql_datetime):
    return mysql_datetime.strftime('%Y-%m-%d %H:%M:%S')



def payload_has_fields(payload, fields):
    keys = list(payload.keys())
    not_present_fields = []

    for field in fields:
        if field not in keys:
            not_present_fields.append(field)

    return len(not_present_fields) == 0



def is_valid_string(string,min,max):

    return isinstance(string,str) and min <= len(string) <= max