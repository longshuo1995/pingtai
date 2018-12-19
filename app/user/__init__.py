from flask import Blueprint


bl_user = Blueprint('user', __name__)
print(111)
from app.user import asset_account
