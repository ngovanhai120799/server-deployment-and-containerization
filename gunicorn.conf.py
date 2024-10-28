import os
from dotenv import load_dotenv

load_dotenv()
workers = os.environ['GUNICORN_PROCESSES']
threads = os.environ['GUNICORN_THREADS']
bind = os.environ['GUNICORN_BIND']

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }