"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = ''
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'easyfind',
        'USER': 'dogukan',
        'PASSWORD': 'krl152..',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
    'easyfind',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION

########## SITE CONFIGURATION
SITE_URL = 'http://localhost:8000'
########## END SITE CONFIGURATION


########## ZEROPUSH CONFIGURATION
ZEROPUSH_AUTH_TOKEN = 'TyjXXmyiai8XAqMyzEsQ'
########## END ZEROPUSH CONFIGURATION


########## MONGO CLIENT CONFIGURATION
MONGO_URI = "mongodb://dogukan:krl152..@oceanic.mongohq.com:10002/easyfind-development"
########## END MONGO CLIENT CONFIGURATION


########## PAYPAL CONFIGURATION
PAYPAL_PWD = 'ATVUGURAFTUCSPN6'
PAYPAL_SIGNATURE = 'AjRpbG13pwOF1c9qbYMVtt3025jKAH7IP4igsr9P4g.SZUfHXYn7et7c'
PAYPAL_USER = 'onurorhan04_api1.gmail.com'
PAYPAL_EMAIL='onurorhan04@gmail.com'
PAYPAL_MODE = 'sandbox'
PAYPAL_CLIENT_ID = 'AejOzhC_VvajEjTWdfpzGEYFgvs_sAP3Bi6iGwnOGpSLJBJKfT5ofp03KK0h'
PAYPAL_CLIENT_SECRET = 'EAyF3hCuvxIxZ9MMLMvyx_FWvkz-0xyzeAOhmbWs2nop_fUeQDaX8dbomlYi'

PAYPAL_RETURN_URL = "http://easyfindapp.herokuapp.com/api/transactions/success/"
PAYPAL_CANCEL_URL = "http://easyfindapp.herokuapp.com/api/transactions/error/"

# sandbox
PAYPAL_URL = 'https://www.sandbox.paypal.com/au/cgi-bin/webscr'
PAYPAL_PDT_URL = 'https://www.sandbox.paypal.com/au/cgi-bin/webscr'
########## END PAYPAL CONFIGURATION