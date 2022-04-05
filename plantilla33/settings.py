"""
Django settings for plantilla33 project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import json
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rx1(2xedv2wxs^&gl0zc#hxgv(3^#=7n6&&w_i8v)ec!3omf@f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'smartagrocol.org']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # OWN APPS
    'plantilla33_app',
    'login_reg_app',
    'core',
    'social_django', #registro con google, twitter, facebook...etc
    'django_extensions', #para usar openssl
    'werkzeug_debugger_runserver',
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

ROOT_URLCONF = 'plantilla33.urls'

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

WSGI_APPLICATION = 'plantilla33.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'plantilla33_app:dashboard' #pagina destino cuando se logea por google

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#autenticacion para la el registro y validacion de google. Hashes
AUTHENTICATION_BACKENDS=['social_core.backends.google.GoogleOAuth2',
                        'django.contrib.auth.backends.ModelBackend',
                        'social_core.backends.facebook.FacebookOAuth2',
                        'social_core.backends.github.GithubOAuth2',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '571772451183-dl11hfafimrp190bcktl52982lc34b1a.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'  

SOCIAL_AUTH_GITHUB_KEY = 'b698e9a1d1203c968588'
SOCIAL_AUTH_GITHUB_SECRET = '144347bbc318803c5431b6fed477e4825c10e9f3' 

# SMTP 
# GMAIL : STMP 
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '86496e76dcd8b4'
# EMAIL_HOST_PASSWORD = '030c6943d188fd'
# EMAIL_PORT = '2525'

EMAIL_SETTINGS_FILE = os.path.join(BASE_DIR, 'emailtrap_settings.json')
with open(EMAIL_SETTINGS_FILE) as data_file:
    emailtrap_settings = json.load(data_file)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = emailtrap_settings['EMAIL_HOST']
EMAIL_HOST_USER = emailtrap_settings['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = emailtrap_settings['EMAIL_HOST_PASSWORD']
EMAIL_PORT = emailtrap_settings['EMAIL_PORT']



# EMAIL_SETTINGS_FILE = os.path.join(BASE_DIR, 'email_settings.json')
# with open(EMAIL_SETTINGS_FILE) as data_file:
#     email_settings = json.load(data_file)

# EMAIL_HOST= email_settings['EMAIL_HOST']
# EMAIL_PORT = email_settings['EMAIL_PORT']
# EMAIL_USE_TLS = email_settings['EMAIL_USE_TLS']
# DEFAULT_FROM_EMAIL = 'smartagro'
# SERVER_EMAIL = 'smartagro'
# EMAIL_HOST_USER = email_settings['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = email_settings['EMAIL_HOST_PASSWORD']

# EMAIL_HOST= 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'ingenieroteleco'
# SERVER_EMAIL = 'ingenieroteleco'
# EMAIL_HOST_USER ="ingenieroteleco@gmail.com"
# EMAIL_HOST_PASSWORD = "Noviembre2020*"