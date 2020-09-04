from getdinerotoday.settings.settings import *

DEBUG = True

SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.veebimajutus.ee'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'getdinerotoday@vash.ee'
EMAIL_HOST_PASSWORD = 'epJ,o0p754'
DEFAULT_FROM_EMAIL = 'info@getdinerotoday.com'

STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', "sk_test_51GadadExWTjX75uFGi8HJDnVtz1xsoPqSlVu5C1HQNK5DjdN9ANTXlxinjF9hF7UffAcRpwfOcDtXbxw4jTi8jIk00TqleQ5pg")

ALLOWED_HOSTS = ['*']
