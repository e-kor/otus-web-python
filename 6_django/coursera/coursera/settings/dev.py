from .base import *
import logging

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_dev.sqlite3'),
    }
}
INSTALLED_APPS.append('debug_toolbar')
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
logging.basicConfig(level=logging.DEBUG)