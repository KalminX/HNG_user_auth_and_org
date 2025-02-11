import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
CSRF_trusted_origins = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

connection_string = os.environ["AZURE_POSTGRESQL_CONNECTIONSTRING"]
parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backend.postgresql',
        'NAME': parameters['dbname'],
        "HOST": parameters['host'],
        "USER": parameters['user'],
        "PASSWORD": parameters['password']
    }
}
