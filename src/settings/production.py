# -*- coding: utf-8 -*-
# production.py
from .base import *
import os

DEBUG = False
PREPEND_WWW = False

# DIRS
STATIC_URL = '/static/'
STATIC_ROOT = "/static/"

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'


ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS', '')

# SESSIONS

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': '300',
    }
}
CKEDITOR_JQUERY_URL = '{}admin/js/vendor/jquery/jquery.js'.format(STATIC_URL)
