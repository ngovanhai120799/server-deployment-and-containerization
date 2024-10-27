import functools
import os
from datetime import datetime, timedelta

import jwt
from flask import request, abort
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.environ['JWT_SECRET']

def require_jwt(f):
    """
    Decorator to check valid jwt is present.
    """
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        decode_jwt()
        return f(*args, **kwargs)
    return decorated_function

def encoded_jwt(body):
    exp_time = datetime.now() + timedelta(days=1)
    payload = {
        'exp': exp_time,
        'nbf': datetime.now(),
        'email': body.get('email')
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def decode_jwt():
    """
    Check user token and return non-secret data
    """
    if not 'Authorization' in request.headers:
        abort(401)
    data = request.headers['Authorization']
    token = str.replace(str(data), 'Bearer', '')
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    except: # pylint: disable=bare-except
        abort(401)