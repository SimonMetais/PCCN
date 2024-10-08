import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

IN_PROD = os.environ.get('IN_PROD')
if IN_PROD:
    print("SETTINGS DE PROD")
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
else:
    print("SETTINGS DE DEV")
DEBUG = True

ALLOWED_HOSTS = ['poneys-chevaux-chez-nous.fr', 'www.poneys-chevaux-chez-nous.fr', '217.160.48.69'] if IN_PROD else ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.poneys-chevaux-chez-nous.fr']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cleanup.apps.CleanupConfig',
    'rangefilter',
    'admin_totals',

    'base',
    'kpi',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'kpi.middleware.kpi_middleware',
]

ROOT_URLCONF = 'django_app.urls'

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

                'base.views.global_context.global_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_app.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'db_name:test',
        "USER": 'db_user:test',
        "PASSWORD": 'db_password:test',
        "HOST": 'PCCN__db',
    } if IN_PROD else {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.parent / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.parent / 'media' if IN_PROD else BASE_DIR / 'media_dev'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_COOKIE_AGE = 30 * 60  # 30 minutes
SESSION_SAVE_EVERY_REQUEST = True
