"""
Django main settings for django_test project.

If you need to override a setting locally, use local.py
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))

TEMPLATE_DEBUG = DEBUG


SECRET_KEY = os.environ['SECRET_KEY']


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

    # Database migrations
    'south',

    # Application base, containing global templates.
    'english.apps.dictionary',
    'english.apps.account',

    # Local apps, referenced via english.appname

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

ROOT_URLCONF = 'english.urls'

WSGI_APPLICATION = 'english.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

APPEND_SLASH = False




# Third-party apps settings

# easy-thumbnails
THUMBNAIL_SUBDIR = 'thumbs'


