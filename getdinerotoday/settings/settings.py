import os

import django_heroku
from django.utils.log import DEFAULT_LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_HOSTCONF = 'getdinerotoday.hosts'
DEFAULT_HOST = 'www'
ROOT_URLCONF = 'getdinerotoday.urls'
LOGIN_URL = '/user/login'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
CORS_ORIGIN_ALLOW_ALL = True
WSGI_APPLICATION = 'getdinerotoday.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

X_FRAME_OPTIONS = 'SameOrigin'
SECURE_REFERRER_POLICY = 'strict-origin'
EMAIL_BACKEND = 'django_amazon_ses.EmailBackend'
AWS_DEFAULT_REGION = 'eu-central-1'
DEFAULT_FROM_EMAIL = 'Getdinerotoday@gmail.com'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
AWS_ACCESS_KEY_ID = "AKIA5YAXFMAOY2WTTGN4"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = 'getdinerotodaybucket2'
AWS_S3_REGION_NAME = 'us-east-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None

DEFAULT_LOGGING['handlers']['console']['filters'] = []

INSTALLED_APPS = [
    'django_hosts',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'business',
    'financing_portal',
    'portals.cannabis',
    'portals.fitness',
    'portals.insurance_agent',
    'portals.musician',
    'portals.restaurant_catering',
    'portals.wedding_planner',
    'portals.accountant',
    'portals.credit_repair',
    'portals.hair_salon',
    'portals.lawyer',
    'portals.photography',
    'portals.transportation',
    'portals.automotive',
    'portals.ecommerce',
    'portals.handy_man',
    'portals.medical',
    'portals.real_estate',
    'portals.trucking',
    'import_export',
    'loanportal',
    'businesscreditcourse',
    'marketingcourse',
    'yourplan',
    'whitelabelpartnerportal',
    'creditcourse',
    'covid19',
    'affiliate',
    'storages',
    'goals',
    'products',
    'onlinetools',
    'dynamic',
    'orders',
    'chromeextension',
    'onboarding',
    'corsheaders',
]

MIDDLEWARE = [
    'getdinerotoday.middleware.hosts.HostsRequestMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'getdinerotoday.middleware.hosts.HostsResponseMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 'user/templates', 'business/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'getdinerotoday.contexts.ProfileProcessor',
                'getdinerotoday.contexts.whitelabel_processor',

            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication'],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Activate Django-Heroku.
django_heroku.settings(locals())
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'