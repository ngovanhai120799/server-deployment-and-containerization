import functools
from datetime import datetime, timedelta, timezone

import jwt
from flask import request, abort
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = "01JB605V4B7DH1BHXRBPQ5GR2N"
JWT_ALGORITHM = 'HS256'

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
    exp_time = datetime.now(tz=timezone.utc) + timedelta(hours=1)
    payload = {
        'exp': exp_time,
        'nbf': datetime.now(tz=timezone.utc),
        'email': body.get('email')
    }
    return jwt.encode(payload, JWT_SECRET)

def decode_jwt():
    """
    Check user token and return non-secret data
    """
    if not 'Authorization' in request.headers:
        abort(401)
    data = request.headers['Authorization']
    token = str.replace(str(data), 'Bearer ','')
    try:
        response = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return response
    except Exception as e: # pylint: disable=bare-except
        abort(401)