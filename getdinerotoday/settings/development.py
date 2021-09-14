from getdinerotoday.settings.settings import *
from dotenv import dotenv_values
config = dotenv_values(".env")

DEBUG = True

SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'
STRIPE_PUBLISHABLE_KEY = os.environ.get(
    'STRIPE_PUBLISHABLE_KEY') if not DEBUG else config['STRIPE_PUBLISHABLE_KEY']
STRIPE_SECRET_KEY = os.environ.get(
    'STRIPE_SECRET_KEY') if not DEBUG else config['STRIPE_SECRET_KEY']
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': True,
}
ALLOWED_HOSTS = ['*']
