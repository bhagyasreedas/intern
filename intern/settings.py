from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+m70a)nce5vhz(i3p**hmoz%=dwo$&&aio^$@v--4aos6r-+e3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'crispy_forms',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'rest_framework',
    'rest_framework.authtoken',
    #'django_expiring_token',
    'users',
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

ROOT_URLCONF = 'intern.urls'

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

WSGI_APPLICATION = 'intern.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
REST_FRAMEWORK = {  
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        #'django_expiring_token.authentication.ExpiringTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}



EXPIRING_TOKEN_DURATION = timedelta(days=90)


# OAUTH2_PROVIDER = {
#     "OIDC_ENABLED": True,
#     "OIDC_RSA_PRIVATE_KEY": os.environ.get("OIDC_RSA_PRIVATE_KEY"),
#     "SCOPES": {
#         "openid": "OpenID Connect scope",
#         # ... any other scopes that you use
#     },
#     # ... any other settings you want
# }


OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "SCOPES": {
        "openid": "OpenID Connect scope",
        'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups',
          'introspection': 'Introspect token scope',
          
        

        # ... any other scopes that you use
    },
      'CLIENT_ID_GENERATOR_CLASS': 'oauth2_provider.generators.ClientIdGenerator',
       'RESOURCE_SERVER_INTROSPECTION_URL': 'http://127.0.0.1:8000/o/introspect/',
    #'RESOURCE_SERVER_AUTH_TOKEN': '3yUqsWtwKYKHnfivFcJu', # OR this but not both:
    # 'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': ('rs_client_id','rs_client_secret'),
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS':('bGdjiXg0LfhVnEWCAaEiPiw1XGdXVXlMDJbUlk0E','nlyuXEbBqaZYLoa9seBP1FvFRL8xk3MiZNkNqetQvXDajSRszNm1THIRtwy3dfTJuyxQZgsDUFxqdHEcfpZu0V9vQB5zwHFvUfLHxKtbnm43NJCNbm21wIj29MKeZ6UP')
    # ... any other settings you want
}