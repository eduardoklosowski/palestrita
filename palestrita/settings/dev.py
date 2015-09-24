# -*- coding: utf-8 -*-

import os
from .core import *  # NOQA

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'palestrita'
DEBUG = True
ALLOWED_HOSTS = []

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
COMPRESS_ROOT = os.path.join(BASE_DIR, 'compress')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    import debug_toolbar  # NOQA
    INSTALLED_APPS += (
        'debug_toolbar',
    )
except ImportError:
    pass
