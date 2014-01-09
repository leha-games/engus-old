
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)


INSTALLED_APPS = (
    # Django contrib apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps, patches, fixes
    'pytils',
    'easy_thumbnails',
    'rest_framework',
    'django_extensions',

    # Database migrations
    'south',

    # Application base, containing global templates.
    'engus.apps.dictionary',
    'engus.apps.cards',

    # Local apps, referenced via engus.appname

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

ROOT_URLCONF = 'engus.urls'

WSGI_APPLICATION = 'engus.wsgi.application'


# Internationalization

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Media and Static Files

MEDIA_ROOT = '/var/webapps/engus/www/media/'

MEDIA_URL = '/media/'

STATIC_ROOT = '/var/webapps/engus/www/static/'

STATIC_URL = '/static/'



APPEND_SLASH = False


# Third-party apps settings

# easy-thumbnails
THUMBNAIL_SUBDIR = 'thumbs'

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

from .local_settings import *