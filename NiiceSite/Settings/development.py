# -*- coding: utf-8 -*-
from .base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'niicesite_dev_db',
        'USER': 'niicesite',
        'PASSWORD': '3Ngl3f13ldh4v3n',
        'HOST': '',
        'PORT': '',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
