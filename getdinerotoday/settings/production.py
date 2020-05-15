import dj_database_url
from getdinerotoday.settings.settings import *

DEBUG = False

# SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'
SECRET_KEY = os.environ.get('SECRET_KEY', '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki')


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'getdinerotoday.herokuapp.com', 'test-dinero-today.herokuapp.com']


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
