# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = u'/home/stevecrooke/NiiceSite/media'
MEDIA_URL = '/media/'
STATIC_ROOT = u'/home/stevecrooke/NiiceSite/static'
STATIC_URL = '/static/'
SECURE_SSL_REDIRECT = True