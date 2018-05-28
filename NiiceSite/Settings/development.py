# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = get_env_variable('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': get_env_variable('DATABASE_HOST'),
        'PORT': get_env_variable('DATABASE_PORT'),
    }
}
