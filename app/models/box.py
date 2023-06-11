from app.db import db
from mysql.connector import IntegrityError

class BoxModel:

    def get_boxes_by_user_id(self, user_id):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM boxes WHERE box_owner = %s",[user_id])
        boxes = cursor.fetchall()
        cursor.close()
        return boxes

    def get_box_by_user_id_and_name(self, user_id, box_name):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM boxes WHERE box_owner = %s AND box_name = %s",[user_id,box_name])
        box = cursor.fetchall()
        cursor.close()
        return box[0] if len(box) > 0 else None

    def create_box(self,user_id,box_name):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute(f"INSERT INTO boxes (box_owner,box_name) VALUES (%s,%s)", [user_id,box_name])
            db.commit()
            cursor.close()
            return {"created_id": cursor.lastrowid}
        except IntegrityError:
            return "duplicated"

    def delete_box(self, user_id, box_name):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"DELETE FROM boxes WHERE box_owner = %s AND box_name = %s", [user_id,box_name])
        db.commit()
        cursor.close()
        return {"deleted_id": cursor.lastrowid}
