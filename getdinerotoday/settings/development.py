from getdinerotoday.settings.settings import *

DEBUG = False

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
ALLOWED_HOSTS = ['*']
