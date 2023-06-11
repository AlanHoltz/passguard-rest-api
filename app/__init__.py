from flask import Flask
from os import getenv
from flask_jwt_extended import JWTManager
import datetime

app = Flask(__name__)

#Configuration of JWT Token Feature for sessions
app.config["JWT_SECRET_KEY"] = getenv("JWT_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=120)
jwt = JWTManager(app)
