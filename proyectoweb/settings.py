"""
Django settings for proyectoweb project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1y#khp5bzd!2*s_+xo=od)z7w_-c71*1fq8^tt#ln!w1ybj3=!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DEFAULT ENGINE FOR EMAILS
DEFAULT_FROM_EMAIL = "postmaster@sandbox210394da446d43899409579c7f7cbe83.mailgun.org"

#EMAIL_HOST = "smtp.mailgun.org"
#EMAIL_HOST_USER = "postmaster@sandbox210394da446d43899409579c7f7cbe83.mailgun.org"    
#EMAIL_HOST_PASSWORD = "0dfc12d7003557af42daa79c05c97260-baa55c84-58062540"
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "albertoj1606@gmail.com"
EMAIL_HOST_PASSWORD = "Thechukrok1606"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


AUTH_USER_MODEL = 'accounts.Account'

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'bootstrap_modal_forms',
    'accounts',
    'Activities',
    'Report',
    'ReportAdmin',
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


ROOT_URLCONF = 'proyectoweb.urls'

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

WSGI_APPLICATION = 'proyectoweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testing2',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'accounts.validators.MinimumLengthValidator',
    },
    {
        'NAME': 'accounts.validators.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
TEMP = os.path.join(BASE_DIR, 'temp')
