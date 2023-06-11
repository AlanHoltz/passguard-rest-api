from dotenv import load_dotenv
load_dotenv()
from app import app
from app.routes.user import user
from app.routes.box import box
from app.routes.account import account
app.register_blueprint(user,url_prefix="/users")
app.register_blueprint(box,url_prefix="/users/boxes")
app.register_blueprint(account,url_prefix="/users/boxes/<string:box_name>/accounts")