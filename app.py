# pylint: disable=import-error
from flask import Flask, jsonify, request, Blueprint
from utils.logging_utils import get_logger, LOG_LEVEL
from decorator import  decode_jwt, require_jwt, encoded_jwt

api = Blueprint('api', __name__)

logger = get_logger()
logger.debug("Starting with log level: %s" % LOG_LEVEL )

@api.route('/', methods=['GET', 'POST'])
def health():
    return jsonify('Healthy')

@api.route('/auth', methods=['GET','POST'])
def auth():
    """
    Create JWT token based on email.
    """
    request_data = request.get_json()
    email = request_data.get('email')
    password = request_data.get('password')
    if not email:
        logger.error('No email provided')
        return jsonify({'message': 'Missing parameter: email'}, 400)
    if not password:
        logger.error('No password provider')
        return jsonify({'message': 'Missing parameter: password'}, 400)
    body = {'email': email, 'password': password}
    token = encoded_jwt(body)
    return jsonify(token)

@api.route('/contents', methods=['GET'])
@require_jwt
def get_content():
    data = decode_jwt()
    return jsonify(data)

def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
if __name__ == '__main__':
    app = create_app()
    app.run()