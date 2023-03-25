import os

from .settings import *


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

POSRGRES_DB = os.getenv('DJANGO_POSTGRES_DB')
POSTGRES_USER = os.getenv('DJANGO_POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('DJANGO_POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('DJANGO_POSTGRES_HOST')
POSTGRES_PORT = os.getenv('DJANGO_POSTGRES_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSRGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}
