# -*- coding: utf-8 -*-
# production.py
from .base import *
import os

DEBUG = False
PREPEND_WWW = False

# DIRS
print("ENTRE AL PRODUCTION @@@@@@@@@@@@@")
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


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
