# -*- coding: utf-8 -*-

import os
from palestrita.settings.core import *  # NOQA

BASE_DIR = os.environ['OPENSHIFT_DATA_DIR']

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
DEBUG = False
ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS']]

TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')
BOWER_COMPONENTS_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'components')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
