__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

import os
from MountainHacks import secrets


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

SECRET_KEY = secrets.SECRET_KEY
DEBUG = True
TEMPLATE_DEBUG = True

CORS_ORIGIN_WHITELIST = (
    'mountainhacks.com',
    'localhost:9000'
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'X-MOUNTAINHACKS'
)

CORS_ALLOW_METHODS = ('POST')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'south',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    #'log_request_id.middleware.RequestIDMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'MountainHacks.urls'

WSGI_APPLICATION = 'MountainHacks.wsgi.application'

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = secrets.EMAIL_USER
EMAIL_HOST_PASSWORD = secrets.EMAIL_PASSWORD
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Mountain'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = '/home/darguetap/webapps/mountainhacks_static/'
STATIC_URL = '/static/'

MEDIA_ROOT = ""
MEDIA_URL = "/"

TEMPLATE_DIRS  = (
    PROJECT_PATH + "/templates/"
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
