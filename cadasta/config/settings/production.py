import os
from .default import *  # NOQA


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cadasta',
        'USER': 'cadasta',
        'PASSWORD': 'cadasta',
        'HOST': os.environ['DB_HOST']
    }
}

DJOSER.update({  # NOQA
    'DOMAIN': os.environ['DOMAIN'],
})

# Adding localhost here for uWSGI debugging!
ALLOWED_HOSTS = [os.environ['API_HOST'], 'localhost']

ADMINS = [('Cadasta platform admins', 'platform-admin@cadasta.org')]
EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
SERVER_EMAIL = 'platform-errors@cadasta.org'
DEFAULT_FROM_EMAIL = 'platform@cadasta.org'

# Debug logging...
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}