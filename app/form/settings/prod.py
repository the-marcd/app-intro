import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proddb',
        'HOST': 'backenddb.cxdsfyihzdq5.us-east-2.rds.amazonaws.com',
        'USER': 'dbuser',
        'PORT': '5432',
        "OPTIONS": {
            "use_iam_auth": True
        }
    }
}