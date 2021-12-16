from getdinerotoday.settings.settings import *
from dotenv import dotenv_values
config = dotenv_values(".env")

DEBUG = True

SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'
STRIPE_PUBLISHABLE_KEY = "pk_live_51IsMmUKRyGPxBMS0JhipiztTS8ncN5y3c0W4lScY7ksBK0xVFY9T8k3DnVBw8JfqmxwIER6oJqCNOGQox4bZALz400WV2vlw9o"
STRIPE_SECRET_KEY = "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"
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': True,
}
ALLOWED_HOSTS = ['*']
