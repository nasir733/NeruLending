"""
Django settings for getdinerotoday project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Application definition

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
    'chromeextension',
    'corsheaders',
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]


ROOT_HOSTCONF = 'getdinerotoday.hosts'
DEFAULT_HOST = 'www'

ROOT_URLCONF = 'getdinerotoday.urls'
LOGIN_URL = '/user/login'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880

# SUBDOMAIN_URLCONFS = {
#     # None: 'getdinerotoday',  # no subdomain, e.g. ``example.com``
#     # 'www': 'getdinerotoday.urls',
#     # 'test': 'myproject.urls.api',
# }

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

CORS_ORIGIN_ALLOW_ALL = True

WSGI_APPLICATION = 'getdinerotoday.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': '/home/django/django_project/db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_API_KEY = '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'


# SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 465 # 587 #25 or 465
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
# EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = 'info@getdinerotoday.com'
# SERVER_EMAIL = EMAIL_HOST_USER


# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

# Configure AWS S3 here
AWS_ACCESS_KEY_ID = 'AKIA4JHKKGCWEHWUWPGE'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'getdinerotodaybucket'
AWS_S3_REGION_NAME = 'us-east-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Activate Django-Heroku.
django_heroku.settings(locals())
