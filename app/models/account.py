from re import U
from app.db import db
from mysql.connector import IntegrityError

class AccountModel:
    def get_accounts_by_box_owner_and_box_name(self, box_owner,box_name):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM accounts WHERE box_owner = %s AND box_name = %s",[box_owner,box_name])
        accounts = cursor.fetchall()
        cursor.close()
        return accounts

    

    def get_account(self,box_owner,box_name,account_id):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM accounts WHERE box_owner = %s AND box_name = %s AND account_id = %s",
        [box_owner,box_name,account_id])
        account = cursor.fetchall()
        cursor.close()
        return account[0] if len(account) > 0 else None


    def create_account(self,box_owner,box_name,account_data):
        try:
            
            cursor = db.cursor(dictionary=True)

            cursor.execute("""
            SELECT MAX(account_id) INTO @last_id 
            FROM accounts 
            WHERE accounts.box_owner = %s AND accounts.box_name = %s
            """,[box_owner,box_name])
            

            cursor.execute("""
            INSERT INTO accounts (box_owner,box_name,account_id,account_description,account_user,account_password)
            VALUES (%s,%s,@last_id + 1,%s,%s,%s)
            """,[box_owner,box_name,account_data["description"],account_data["user"], account_data["password"]])

            db.commit()
            cursor.close()
            return {"created_id": cursor.lastrowid}
        except IntegrityError:
            return "duplicated"
    


    def delete_account(self,box_owner,box_name,account_id):
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"DELETE FROM accounts WHERE box_owner = %s AND box_name = %s AND account_id = %s", 
        [box_owner,box_name,account_id])
        db.commit()
        cursor.close()
        return {"deleted_id": cursor.lastrowid}       