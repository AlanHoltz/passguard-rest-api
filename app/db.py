from mysql.connector import connect, Error
from os import getenv


try:
    db = connect(
        host="localhost",
        user="root",
        password=getenv("DB_PASSWORD"),
        database="passguard"
    )
except Error as err:
    print(err)
