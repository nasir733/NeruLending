import dj_database_url

from getdinerotoday.settings.settings import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki')

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.veebimajutus.ee'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'getdinerotoday@vash.ee'
EMAIL_HOST_PASSWORD = 'epJ,o0p754'
DEFAULT_FROM_EMAIL = 'info@getdinerotoday.com'
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
