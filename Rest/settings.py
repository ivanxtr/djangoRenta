"""
Django settings for Rest project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ['DEV'] is True:
    DEBUG = True
else:
    DEBUG = True

ALLOWED_HOSTS = ['bodegas-api.herokuapp.com', 'localhost', 'localhost:3000', 'bodegas-react-ssr.herokuapp.com', 'solo-bodegas.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'Bodegas',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Rest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if os.environ['DEV'] is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bodegas',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': 'db',
            'PORT': '3306'
        }
    }
else:
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'zurdnas69vi3mngr',
            'USER': 'njzcprcc1v9ce8q1',
            'PASSWORD': 'mzyttqnm82eu6d5z',
            'HOST': 'dt3bgg3gu6nqye5f.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            'PORT': '3306'
        }
    } 


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://127.0.0.1:9000",
    "https://bodegas-react-ssr.herokuapp.com",
    "http://solo-bodegas.com",
    "https://solo-bodegas.com"
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
