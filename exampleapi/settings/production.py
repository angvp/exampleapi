from .base import *  # noqa
import os


DEBUG = False
TEMPLATES['OPTIONS']['debug'] = DEBUG

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

ADMINS = (
    ('Angel Velasquez', 'angvp@archlinux.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'exampleapi',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': '',
    }
}
