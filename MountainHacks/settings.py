__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

import os
from MountainHacks import secrets
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = secrets.SECRET_KEY
DEBUG = True
TEMPLATE_DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'south',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MountainHacks.urls'

WSGI_APPLICATION = 'MountainHacks.wsgi.application'

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Mountain'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
