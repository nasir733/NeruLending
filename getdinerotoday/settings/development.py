from getdinerotoday.settings.settings import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.veebimajutus.ee'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'getdinerotoday@vash.ee'
EMAIL_HOST_PASSWORD = 'epJ,o0p754'
DEFAULT_FROM_EMAIL = 'info@getdinerotoday.com'

STRIPE_PUBLISHABLE_KEY = 'pk_test_k8aDNdIlHgXwyIJIf1tswxny00h0Xyel4S'
STRIPE_SECRET_KEY = 'sk_test_ZZa6QOdZS7mz9Xo17MxQHRgM00ozbxBI5g'

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'getdinerotoday.herokuapp.com', '*']
