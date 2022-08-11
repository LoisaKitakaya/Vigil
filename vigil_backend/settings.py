"""
Django settings for vigil_backend project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta

# cors headers

from corsheaders.defaults import default_methods
from corsheaders.defaults import default_headers

# cloudinary

import cloudinary
import cloudinary.uploader
import cloudinary.api

# force_text is removed from Django 4.0
# to fix force_text import error

import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=v9j=xy^zk3ql6m3$y-bzomr+v&6(e))ugqjimp@nd0^7u9*^i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # my apps
    'users',
    'products',
    'orders',
    'core',
    'cart',

    # 3rd party apps
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'corsheaders',
    'django_quill',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # cors headers middleware
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vigil_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # custom context processors
                'products.context_processors.all_categories',
                'orders.context_processors.delivery_cost',
                'orders.context_processors.pickup_cost',
                'products.context_processors.all_tags',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'vigil_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom settings

# Custom user model

AUTH_USER_MODEL = 'users.User'

# cart sessions

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

# default redirect routes

LOGIN_URL = '/accounts/sign_in/'
LOGIN_REDIRECT_URL = '/products/'
LOGOUT_REDIRECT_URL = '/'

# cloudinary config

cloudinary.config( 
  cloud_name = "dit0fii18", 
  api_key = "488158286488541", 
  api_secret = "15AEbpxsXhNF828AaNQtQy7iOR0",
  secure = True
)

# graphene-django settings

GRAPHENE = {
    "SCHEMA": "vigil_backend.schema.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

# django graphql jwt settings

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
}

# CORS headers settings

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
]

CORS_ALLOW_METHODS = list(default_methods)

CORS_ALLOW_HEADERS = list(default_headers)
