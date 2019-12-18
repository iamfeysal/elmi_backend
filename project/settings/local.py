from project.settings.base import *  # noqa

from decouple import config, Csv
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
    )
}

if config('MODE') == "dev":
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'eccomas',
    #         'USER': 'root',
    #         'PASSWORD': 'fazmandinho',
    #         'HOST': 'localhost',
    #         'PORT': '',
    #     }
    # }

    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', cast=bool)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': '',
        }
    }

CORS_ORIGIN_ALLOW_ALL = True

# DEBUG = config('DEBUG', default=True, cast=bool)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': '',
#     }
# }
