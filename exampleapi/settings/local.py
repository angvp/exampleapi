from .base import *  # noqa


ADMINS = (
    ('Angel Velasquez', 'angvp@archlinux.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'exampleapi_test.db',
    }
}
