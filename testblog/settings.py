"""
Django settings for testblog project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# connect('mongodb+srv://datisekai:yvCd9dQgXWCTEcmk@cluster0.fh43eys.mongodb.net/Cluster0?retryWrites=true&w=majority')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-fcr!5zj&dqba6gcj69$0k7)yk)bix)86kcr%bd6y@&ig(pl&io"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'src',
    'ckeditor',
    'ckeditor_uploader',
    'mongoengine',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "testblog.urls"
LOGOUT_REDIRECT_URL = "/login"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "testblog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    # 'default': {
    #     'ENGINE': 'mongoengine',
    #     'NAME': 'Cluster0',
    #     'ENFORCE_SCHEMA': False,
    #     'CLIENT': {
    #             'host': 'mongodb+srv://datisekai:yvCd9dQgXWCTEcmk@cluster0.fh43eys.mongodb.net/Cluster0?retryWrites=true&w=majority'
    #     }
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.dummy',
    # },
    # 'mongo': {
    #     'ENGINE': 'django_mongodb_engine',
    #     'NAME': 'Cluster0',
    #     'HOST': 'cluster0.fh43eys.mongodb.net',
    #     "USERNAME":"datisekai",
    #     "PASSWORD":"yvCd9dQgXWCTEcmk"
    # }
    # 'default': {
    #     'ENGINE': 'djongo',
    #     'NAME': 'Cluster0',
    #     'ENFORCE_SCHEMA': True,
    #     'CLIENT': {
    #             'host': 'mongodb+srv://datisekai:yvCd9dQgXWCTEcmk@cluster0.fh43eys.mongodb.net/Cluster0?retryWrites=true&w=majority'
    #     }
    # }
    # 'default': {  
    #     'ENGINE': 'django.db.backends.mysql',  
    #     'NAME': 'testblog',  
    #     'USER': '2posdz5b9ydr74wc5p2w',  
    #     'PASSWORD': 'pscale_pw_kIABprjV1AecJBJZWaQ9ujUWT0uIWbpBjN948LhlBLk',  
    #     'HOST': 'aws.connect.psdb.cloud',  
    #     'PORT': '3306',  
    #     'OPTIONS': {  
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #         'ssl': {
    #             'rejectUnauthorized': True,
    #         },  
    #         'charset': 'utf8mb4'
    #     }  
    # }  
    # 'default': {  
    #     'ENGINE': 'django.db.backends.mysql',  
    #     'NAME': 'testblog',  
    #     'USER': 'root',  
    #     'PASSWORD': '',  
    #     'HOST': 'localhost',  
    #     'PORT': '3306',  
    #     'OPTIONS': {  
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     }  
    # }  
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testblog_142r',
        'USER': 'datisekai',
        'PASSWORD': 'DVOXW3ZmuMWC0wLtt0oeJv12rSS1iCxM',
        'HOST': 'dpg-cgs20002qv20m9n18njg-a.singapore-postgres.render.com',
        'PORT': '5432',
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# CKEDITOR
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_UPLOAD_PATH = "uploads/"
STATIC_ROOT = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
