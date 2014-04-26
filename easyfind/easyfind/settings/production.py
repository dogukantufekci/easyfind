"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['easyfindapp.herokuapp.com', ]
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
def get_cache():
    try:
        environ['MEMCACHE_SERVERS'] = environ['MEMCACHIER_SERVERS']
        environ['MEMCACHE_USERNAME'] = environ['MEMCACHIER_USERNAME']
        environ['MEMCACHE_PASSWORD'] = environ['MEMCACHIER_PASSWORD']
        return {
            'default': {
                'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                'LOCATION': environ['MEMCACHIER_SERVERS'],
                'TIMEOUT': 500,
                'BINARY': True,
            }
        }
    except:
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
            }
        }


CACHES = get_cache()
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## API SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
API_SECRET_KEY = get_env_setting('API_SECRET_KEY')
########## END API SECRET CONFIGURATION


########## SITE CONFIGURATION
SITE_URL = 'http://easyfindapp.herokuapp.com'
########## END SITE CONFIGURATION


########## AWS S3 CONFIGURATION
DEFAULT_FILE_STORAGE = '%s.s3utils.MediaS3BotoStorage' % SITE_NAME
STATICFILES_STORAGE = '%s.s3utils.StaticS3BotoStorage' % SITE_NAME

AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_setting('AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY)
}
########## END AWS S3 CONFIGURATION


# ########## COMPRESSION CONFIGURATION
# # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
# COMPRESS_OFFLINE = True

# # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
# COMPRESS_STORAGE = DEFAULT_FILE_STORAGE

# # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
# COMPRESS_CSS_FILTERS += [
#     'compressor.filters.cssmin.CSSMinFilter',
# ]

# # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
# COMPRESS_JS_FILTERS += [
#     'compressor.filters.jsmin.JSMinFilter',
# ]
# ########## END COMPRESSION CONFIGURATION


########## ZEROPUSH CONFIGURATION
ZEROPUSH_AUTH_TOKEN = '3EZttS4bxS3379KGb65G'
########## END ZEROPUSH CONFIGURATION


########## MONGO CLIENT CONFIGURATION
MONGO_URI = "mongodb://dogukan:krl152..@oceanic.mongohq.com:10002/easyfind-production"
########## END MONGO CLIENT CONFIGURATION