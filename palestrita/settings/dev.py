# -*- coding: utf-8 -*-

import os
from .core import *  # NOQA

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'palestrita'
DEBUG = True
ALLOWED_HOSTS = []

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
