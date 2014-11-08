__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

import os
from MountainHacks import secrets
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
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

ROOT_URLCONF = 'MountainHacks.urls'

WSGI_APPLICATION = 'MountainHacks.wsgi.application'

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
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

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )



# Support for X-Request-ID
# https://devcenter.heroku.com/articles/http-request-id-staging

# LOG_REQUEST_ID_HEADER = 'HTTP_X_REQUEST_ID'
# LOG_REQUESTS = True
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'request_id': {
#             '()': 'log_request_id.filters.RequestIDFilter'
#         }
#     },
#     'formatters': {
#         'standard': {
#             'format': '%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'filters': ['request_id'],
#             'formatter': 'standard',
#         },
#     },
#     'loggers': {
#         'log_request_id.middleware'
STATIC_ROOT = '/home/darguetap/webapps/mountainhacks_static/'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
