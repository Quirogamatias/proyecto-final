from .base import *
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DEBUG = False
DEBUG = True

#ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['277e-179-62-84-59.sa.ngrok.io'] esto se cambia segun la url que te de ngrok, siempre tiene que estar en funcionamiento la aplicacion
ALLOWED_HOSTS = ['saipes.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3mu5hlft2vl6s',
        'USER': 'aetwvpoqrmoozt',
        'PASSWORD': '448d8e4b7f86458367c55093332cf0c0d666d9c55611697256509a6dfad2cd52',
        'HOST': 'ec2-54-165-178-178.compute-1.amazonaws.com',
        'PORT': 5432
    }