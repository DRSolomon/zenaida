"""
Django settings for foo project.

Generated by 'django-admin startproject' using Django 1.9.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from __future__ import unicode_literals

import os

from main import params

#------------------------------------------------------------------------------ 
#--- BASE DJANGO SETTINGS
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = '/home/zenaida/live/current'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
REPO_ROOT = os.path.dirname(SRC_PATH)
CONTENT_DIR = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
DEBUG = getattr(params, 'DEBUG', False)
DEBUGTOOLBAR_ENABLED = False
METRICS_ENABLED = False
CACHE_BACKEND = 'redis_cache.RedisCache'
CACHE_LOCATION = '127.0.0.1:6379'

CACHE_PREFIX = 'zenaida'

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = getattr(params, 'SECRET_KEY', 'must be declared in src/main/params.py directly  !')

ALLOWED_HOSTS = ['*']

SITE_ID = 1

ROOT_URLCONF = 'main.urls'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    },
    'root': {
        'level': 'DEBUG' if DEBUG else 'WARNING',
        'handlers': ['console', ],
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
        'timestamped': {
            'format': '%(levelname)s %(asctime)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': [],
        },
        'epp': {
            'propagate': False,
        } if not getattr(params, 'EPP_LOG_FILENAME') else  {
            'level': 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename': getattr(params, 'EPP_LOG_FILENAME'),
            'maxBytes' : 1024*1024*10,  # 10MB
            'backupCount' : 10,
            'formatter': 'timestamped',
        },
        'automats': {
            'propagate': False,
        } if not getattr(params, 'AUTOMATS_LOG_FILENAME') else {
            'level': 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename': getattr(params, 'AUTOMATS_LOG_FILENAME'),
            'maxBytes' : 1024*1024*10,  # 10MB
            'backupCount' : 10,
            'formatter': 'timestamped',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['console', ]
        },
        'automats.automat': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['automats', ]
        },
        'zepp.csv_import': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['console', ]
        },
        'zepp.zclient': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['epp', ]
        },
        'pika': {
            'propagate': False,
        },
    }
}

# if DEBUG and os.environ.get('RUN_MAIN', None) != 'true':
#     LOGGING = {}

#------------------------------------------------------------------------------
#--- Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
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


#------------------------------------------------------------------------------
#--- Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


#------------------------------------------------------------------------------
#--- Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#------------------------------------------------------------------------------
#--- Application definition
INSTALLED_APPS = [
    # nice django admin: https://django-grappelli.readthedocs.io/en/latest/
    'grappelli',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # improved amdin: https://django-nested-admin.readthedocs.io/en/latest/quickstart.html
    'nested_admin',
    # html templates: https://django-bootstrap4.readthedocs.io/en/stable/quickstart.html
    'bootstrap4',
    # usefull things: https://django-extensions.readthedocs.io/en/latest/command_extensions.html
    'django_extensions',
    'billing',
    'accounts',
    'back',
    'front',
    'main',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'raven.contrib.django.middleware.SentryLogMiddleware',
    # 'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


#------------------------------------------------------------------------------
#--- Email settings
EMAIL_BACKEND = getattr(params, 'EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = getattr(params, 'EMAIL_HOST', '')
EMAIL_HOST_USER = getattr(params, 'EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = getattr(params, 'EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = getattr(params, 'EMAIL_PORT', 465)
EMAIL_USE_TLS = getattr(params, 'EMAIL_USE_TLS', False)
EMAIL_USE_SSL = getattr(params, 'EMAIL_USE_SSL', True)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


#------------------------------------------------------------------------------
#--- Sentry defaults
SENTRY_DSN = None


#------------------------------------------------------------------------------
#--- STANDALONE ?
ENV = getattr(params, 'ENV')
STANDALONE = True
if ENV in ['production', 'docker', ]:  # pragma: no cover
    STANDALONE = False


#------------------------------------------------------------------------------
#--- DATABASE DEFAULTS
DATABASES_OPTIONS = {}
DATABASES_TEST = {}
DATABASES_CONN_MAX_AGE = 0

# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': getattr(params, 'DATABASES_ENGINE'),
        'NAME': getattr(params, 'DATABASES_NAME'),
        'OPTIONS': DATABASES_OPTIONS,
        'TEST': DATABASES_TEST,
        'CONN_MAX_AGE': DATABASES_CONN_MAX_AGE,
    }
}

# overwrite live settings if something was set in src/main/params.py
for key in ('ENGINE', 'HOST', 'PORT', 'USER', 'PASSWORD'):
    try:
        key_with_prefix = 'DATABASES_{}'.format(key)
        if hasattr(params, key_with_prefix):
            DATABASES['default'][key] = getattr(params, key_with_prefix)
    except KeyError:
        pass


# Caches
CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION,
        'KEY_PREFIX': CACHE_PREFIX
    }
}


#------------------------------------------------------------------------------
#--- Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}


#------------------------------------------------------------------------------
#--- USER LOGIN/AUTH/COOKIE
ENABLE_USER_ACTIVATION = True
LOGIN_VIA_EMAIL = True
LOGIN_REDIRECT_URL = '/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SESSION_COOKIE_NAME = 'zenaida_sid'
CSRF_COOKIE_NAME = 'zenaida_csrftoken'


#------------------------------------------------------------------------------
#--- CUSTOM USER MODEL
# https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
AUTH_USER_MODEL = 'accounts.Account'


#------------------------------------------------------------------------------
#--- django-extensions graph models
# https://django-extensions.readthedocs.io/en/latest/graph_models.html
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


#------------------------------------------------------------------------------
#--- ZENAIDA RELATED CONFIGS
LOADED_OK = 'OK'
DEFAULT_REGISTRAR_ID = getattr(params, 'DEFAULT_REGISTRAR_ID')
SUPPORTED_ZONES = getattr(params, 'SUPPORTED_ZONES')
RABBITMQ_CLIENT_CREDENTIALS_FILENAME = getattr(params, 'RABBITMQ_CLIENT_CREDENTIALS_FILENAME')
