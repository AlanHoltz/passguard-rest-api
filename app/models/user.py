from app.db import db
from mysql.connector import IntegrityError

class UserModel:

    def register_user(self, user_data):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute(f"INSERT INTO users VALUES (NULL,%s,%s,NULL)",[user_data["username"],user_data["password"]])
            db.commit()
            cursor.close()
            return {"created_id": cursor.lastrowid}
        except IntegrityError:
            return "duplicated"

    
    def get_user_by_username(self, username):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM users WHERE user_name = %s",[username])
        user = cursor.fetchall()
        cursor.close()
        return user[0] if len(user) > 0 else None
