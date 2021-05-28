import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'invites.apps.LoggerConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'mikuinvite.urls'

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

WSGI_APPLICATION = 'mikuinvite.wsgi.application'

dotenv_file = BASE_DIR / ".env"
if os.path.isfile(dotenv_file):
    import dotenv
    dotenv.load_dotenv(dotenv_file)

    PRODUCTION_SERVER = False
    DEBUG = True
    SECRET_KEY = '7$xw$^&2rne%#gqm!-n!y$%!7*uahe1cmnc!8hd3j+=syy3=$)'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    import dj_database_url

    PRODUCTION_SERVER = True
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY','SECRET_KEY')
    
    DATABASES = {'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'))}
    MIDDLEWARE = [MIDDLEWARE[0]] + \
        ['whitenoise.middleware.WhiteNoiseMiddleware']+MIDDLEWARE[1:]
    INSTALLED_APPS = INSTALLED_APPS[0:-1] + \
        ['whitenoise.runserver_nostatic',]+[INSTALLED_APPS[-1]]
    


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

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = False

USE_L10N = False

USE_TZ = False

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

if PRODUCTION_SERVER:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = "same-origin"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

PASSWORD = os.environ.get('PASSWORD')
TOKEN = os.environ['TOKEN']

BASE_URI = 'https://discord.com/api/v8'
