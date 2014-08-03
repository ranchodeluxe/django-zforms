import re, os, sys

#
# add ( ../../django-zforms ) directory to the path so we can 
# import zforms, common apps and not make them apps of this project
#
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))

ABSOLUTE_PATH = re.sub( '/example$', '', os.path.dirname( __file__ ) )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's+6otzc3g368^h7i-i+jw638ug_fi#!hf)=28abvf2r&n6=$=v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


TEMPLATE_DIRS = ( 
    os.path.join( ABSOLUTE_PATH, '..', 'zforms', 'templates' ).replace('\\','/'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'common',
    'zforms',
    'example',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        #'HOST': 'mysql10.pugetworks.com',
        'NAME': 'djforms',
        'USER': 'zcrowd',
        'PASSWORD': 'zcrowd',
        'OPTIONS': {
            #'default-character-set': 'utf8',
            #'default-collation': 'utf8_unicode_ci',
            'init_command': 'SET storage_engine=INNODB',
        },  
    },  
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGGING = { 
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }   
    },  
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },  
        'minimal': {
            'format': '%(levelname)s %(module)s %(message)s'
        },  
        'simple': {
            'format': '%(levelname)s %(message)s'
        },  
    },  
    'loggers': {
        '': {
            'handlers': [ 'console', ],
            'level': 'DEBUG',
            'propogate': True,
        },  
    },  
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },  
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'minimal',
        },  
    },  
}

