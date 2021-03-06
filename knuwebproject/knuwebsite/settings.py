"""
Django settings for knuwebsite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eq4k$cq@qx7g^9u1%a-qmt0wmqp4g&mpfj(gtw15d5jipsxb8n'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notice.apps.NoticeConfig',
    'q_n_a.apps.QNAConfig',
    'home.apps.HomeConfig',
    'game.apps.GameConfig',
    'accounts.apps.AccountsConfig',
    'interview.apps.InterviewConfig',
    'gallery.apps.GalleryConfig',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
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

ROOT_URLCONF = 'knuwebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'knuwebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# deploy용 database setting
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'knuwebsite',
#         'USER': 'name',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# local용 database setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# S3를 연동시키기 위해 필요한 설정들
AWS_STORAGE_BUCKET_NAME = "knulikelion7"
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False

# static file들은 그냥 서버에 local로 저장하고 불러온다.
# STATIC_ROOT는 static파일을 어디에 저장할 건지, STATIC_URL은 어디서 static 파일을 가져올 건지
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS는 collectstatic을 했을 때 어디서 가져올 건지 target 폴더들
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home', 'static'),
    os.path.join(BASE_DIR, 'game', 'static'),
    os.path.join(BASE_DIR, 'notice', 'static'),
    os.path.join(BASE_DIR, 'q_n_a', 'static'),
    os.path.join(BASE_DIR, 'interview', 'static'),
]

# local용 media setting
# MEDIA_ROOT는 upload파일을 어디에 저장할 건지, MEDIA_URL은 어디서 upload한 파일을 가져올 건지
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# deploy용 media setting
# MEDIA_URL은 media file(upload한 file)을 어디서 부터 가져올 건지, DEFAULT_FILE_STORAGE는 file들을 어디로 upload할 건지
# MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# heroku server는 postgres로 돌려야 되서 이에 필요한 설정, 위에 import도 같이 주석을 하고 풀어줘야 한다.
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# 신웅이가 주석 달아주겠지?
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_REQUIRE_STAFF=False
# ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
