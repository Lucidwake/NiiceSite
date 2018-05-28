# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
SECRET_KEY='=^4f+np958+$^73-ogoyq4na)glt9(ved!*6kz+zc9tqp=tb*c'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'niicesite_db',
        'USER': 'niicesite',
        'PASSWORD': '3Ngl3f13ldh4v3n',
        'HOST':'',
        'PORT':'',
    }
}
