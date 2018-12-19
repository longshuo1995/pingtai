from app import create_app
from flask_cors import CORS

from conf import setting

app = create_app()

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port=setting.web_port, debug=True)
