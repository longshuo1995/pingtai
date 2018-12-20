from flask import Blueprint


bl_user = Blueprint('user', __name__)

from app.user import asset_account
