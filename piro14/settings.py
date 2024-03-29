"""
Django settings for piro14 project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
# 외부에 있는 secrest.json를 활용해 secrest key 불러오기


### start
secret_file = os.path.join(BASE_DIR, 'secrets.json') #secrets.json을 불러와 줍니다

with open(secret_file, 'r') as f: #open as로 secret.json을 열어줍니다.
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets): #예외 처리를 통해 오류 발생을 검출합니다.
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")
### finish


'''
< 클론 후 단순 프로그램 실행을 하고 싶은 경우 >
1. 위의 start~finish 내용을 주석처리합니다.
2. SECRET_KEY = '.'  <- 왼쪽의 코드를 한 줄 추가합니다.

< runserver 후 소셜로그인 관련 error가 난 경우 >
1. python manage.py createsuperuser 후 admin 페이지 접속
2. 각 소셜로그인(구글,네이버)에 관한 자신의 API 값을 적용합니다.
( 2번 설정 참고 ) https://egg-money.tistory.com/117 '''


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
    'game',

    'django.contrib.sites',

    # allauth에 관한 내용들
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # provider
    'allauth.socialaccount.providers.google' , #구글 로그인
    # 'allauth.socialaccount.providers.kakao' , #카카오 로그인 ( 왜 안되니 ^^ )
    'allauth.socialaccount.providers.naver', #네이버 로그인


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

ROOT_URLCONF = 'piro14.urls'

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

WSGI_APPLICATION = 'piro14.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # 소셜로그인 정보를 User 모델 클래스에 저장
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 2

# django-allauth setting
# 로그인/로그아웃 후 리디렉션 할 페이지
# 'tif:index' 형식으로 쓸 수 있음
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True  # 로그아웃 버튼 클릭 시 자동 로그아웃

# # 이메일 확인을 하지 않음.
SOCIAL_ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'Email'
# ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_USERNAME_REQUIRED=False

