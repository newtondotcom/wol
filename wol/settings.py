###CUSTOM SETTINGS
NB_ITEMS_PER_PAGE=20

###DJANGO RELATED
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL =  "/"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'datas.apps.DatasConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wol.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates','templates/registration'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wol.context_processors.common_context'
            ],
        },
    },
]

AUTH_USER_MODEL = 'datas.CustomUser'

WSGI_APPLICATION = 'wol.wsgi.application'

DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
    'default': {
         'ENGINE': 'django.db.backends.mysql',
          'NAME': os.getenv("DB_NAME"),
          'USER': os.getenv("DB_USER"),
         'PASSWORD': os.getenv("DB_PASSWORD"),
          'HOST': os.getenv("DB_HOST"),
         'PORT': os.getenv("DB_PORT"),
     }
}



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


LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True

import os

STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images')
MEDIA_URL = os.path.join(BASE_DIR, 'static/images/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
