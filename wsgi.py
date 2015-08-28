#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from palestrita.wsgi import application  # NOQA
