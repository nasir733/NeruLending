from getdinerotoday.settings.settings import *
from dotenv import dotenv_values
config = dotenv_values(".env")

DEBUG = True

SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'
STRIPE_PUBLISHABLE_KEY = "pk_live_51GadadExWTjX75uFNZcxdwdGeMvUQCQAnxo1xicutlZd9i90Vn19l2TqPTP607peHTp36hFC1HgcUETm1RcuD7nf00zzcHGsCP"
STRIPE_SECRET_KEY = "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"
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': True,
}
ALLOWED_HOSTS = ['*']
