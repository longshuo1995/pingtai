from app import create_app

from conf import setting

print('ready create..')
app = create_app()
print('create.. success')
print(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=setting.web_port, debug=True)
