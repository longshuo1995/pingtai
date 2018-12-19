from flask import Blueprint


bl_user = Blueprint('user', __name__)

print('import assert_account')
from app.user import asset_account
