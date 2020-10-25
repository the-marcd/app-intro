import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proddb',
        'HOST': '<>',
        'USER': '<>',
        'PASSWORD': '<>',
        'PORT': '3306'
    }
}