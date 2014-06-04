"""
Django settings for webinar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'uy3w-*7l3ip5c#cj*+^ej##($&em2gprmt34%x98_s#juj2$6%'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', 'django.template.loaders.eggs.Loader')
INSTALLED_APPS = ('django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'django_extensions', 'registration', 'registration_defaults', 'entitlements')
MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware')
ROOT_URLCONF = 'webinar.urls'
WSGI_APPLICATION = 'webinar.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, 'templates'),)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static_dest')
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)
AUTH_PROFILE_MODULE = 'entitlements.EntitlementProfile'

