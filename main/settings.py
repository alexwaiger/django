# -*- coding: utf-8 -*-
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z#&wrhn=dyz4tc2fb71!44r*k47d&%6g2hokaf*n)t@vx+-37c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

PWA_APP_DEBUG_MODE = False

ALLOWED_HOSTS = ['*',]

# Application definition

INSTALLED_APPS = [
    'django_admin_listfilter_dropdown',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'colorfield',
    'postbacks',
    'casinos',
    'decor',
    'geo',
    'easy_thumbnails',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en'

SITE_LANGUAGE = 'pl'

LANGUAGES = (
  ('pl', 'PL'),
  ('en', 'EN'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

REFERRER_POLICY = 'strict-origin-when-cross-origin'

THUMBNAIL_QUALITY = 60

THUMBNAIL_ALIASES = {
    '': {
        'site_logo': {'size': (200, 0), 'crop': False, 'quality': 85},
        'site_logo_mini': {'size': (96, 0), 'crop': False, 'quality': 85},
        'icon': {'size': (48, 0), 'crop': False, 'quality': 85},
        'bg_mob': {'size': (480, 0), 'crop': True, 'quality': 40},
        'bg_tab': {'size': (992, 0), 'crop': True, 'quality': 40},
        'bg_desc': {'size': (1280, 0), 'crop': True, 'quality': 40},
        'lazy_icon': {'size': (48, 0), 'crop': False, 'quality': 1},
        'lazy_logo_mini': {'size': (48, 0), 'crop': False, 'quality': 1},
        'lazy_logo': {'size': (200, 0), 'crop': False, 'quality': 1},
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
 
STATIC_URL = '/static/'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'media/js', 'serviceworker.js')

PWA_APP_NAME = 'Casino Bonus'
PWA_APP_DESCRIPTION = 'Best Casino in Poland for Real Money'
PWA_APP_THEME_COLOR = '#111111'
PWA_APP_BACKGROUND_COLOR = '#111111'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/' + SITE_LANGUAGE + '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/' + SITE_LANGUAGE + '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/media/favicons/maskable-icon-512x512.png',
        'sizes': '512x512',
        'purpose': 'maskable'
    },
    {
        'src': '/media/favicons/android-icon-36x36.png',
        'sizes': '36x36',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/android-icon-48x48.png',
        'sizes': '48x48',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/android-icon-72x72.png',
        'sizes': '72x72',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/android-icon-96x96.png',
        'sizes': '96x96',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/android-icon-144x144.png',
        'sizes': '144x144',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/android-icon-192x192.png',
        'sizes': '192x192',
        'purpose': 'any'
    }   
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/media/favicons/apple-icon-57x57.png',
        'sizes': '57x57',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-60x60.png',
        'sizes': '60x60',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-72x72.png',
        'sizes': '72x72',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-76x76.png',
        'sizes': '76x76',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-114x114.png',
        'sizes': '114x114',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-120x120.png',
        'sizes': '120x120',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-144x144.png',
        'sizes': '144x144',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-152x152.png',
        'sizes': '152x152',
        'purpose': 'any'
    },
    {
        'src': '/media/favicons/apple-icon-180x180.png',
        'sizes': '180x180',
        'purpose': 'any'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/media/favicons/splash-640x1136.png',
        'media': '(device-width: 360px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = SITE_LANGUAGE