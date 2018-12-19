from app.user import bl_user
from flask import render_template, request
import time

from db import db_mongo


def get_init_data():
    res = db_mongo.account.qq_account.find()
    data = {
        'msg': 'hi',
        'accounts': []
    }
    for i in res:
        data['accounts'].append(i)
    return data


@bl_user.route('/save_account')
def save_account():
    username = request.args.get('username')
    password = request.args.get('password')
    data = get_init_data()
    if not username or not password:
        data['msg'] = '请输入账号密码'
    elif db_mongo.account.qq_account.find({'account': username.strip()}):
        data['msg'] = '账号已存在~'
    else:
        db_mongo.account.insert_one({
            'account': username,
            'password': password,
            'timestamp': int(time.time()),
        })
        data['msg'] = '提交成功'

    return render_template('user/receive.html', data=data)
