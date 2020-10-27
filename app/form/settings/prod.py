import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proddb',
        'HOST': os.environ("DBINSTANCE"),
        'USER': 'dbuser',
        'PORT': '5432',
        "OPTIONS": {
            "use_iam_auth": True
        }
    }
}