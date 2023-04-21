from .base import *
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['164.90.218.93']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'lean',
        'PASSWORD': 'leanempleado',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# nuevo en DJ 4.2
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR.child('static')]
# STATIC_ROOT = BASE_DIR.child('staticfiles')
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR.child('media')
