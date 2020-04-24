from getdinerotoday.settings.settings import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'testdineroooo.herokuapp.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
