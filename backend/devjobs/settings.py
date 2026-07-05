import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

from django.conf import settings
from django.conf.urls.static import static

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = (
  'django-insecure-sqnb$_(4v)vp*yh#0+rb%md#-4=2hr%f!z849*xp+e%t5lc($_'
)
PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
DEBUG = not PRODUCTION
ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']
AUTH_USER_MODEL = 'jobs.User'
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'apps.jobs',
  'ninja_extra',
  'ninja_jwt',
  'ninja_jwt.token_blacklist',
  'corsheaders',
]

CORS_ALLOWED_ORIGINS = [
  'http://localhost:5173',
  'https://devjobs.vercel.app'
]
MIDDLEWARE = [
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
ROOT_URLCONF = 'devjobs.urls'
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]
WSGI_APPLICATION = 'devjobs.wsgi.app'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('SUPABASE_DATABASE_HOST'),
        'PORT': os.getenv('SUPABASE_DATABASE_PORT'),
        'NAME': os.getenv('SUPABASE_DATABASE_NAME'),
        'USER': os.getenv('SUPABASE_DATABASE_USER'),
        'PASSWORD': os.getenv('SUPABASE_DATABASE_PASSWORD'),
        'OPTIONS': {
            'sslmode': 'require',
    }
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
LANGUAGE_CODE = 'en-es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
NINJA_JWT = {
  # Para que en el /refresh me refresque tambien el refresh token
  'ROTATE_REFRESH_TOKENS': True,
  # Para invalidar refresh tokens
  'BLACKLIST_AFTER_ROTATION': True,
  'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}