from .base import *  #noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB', 'restaurant_local'),
        'USER': env.str('POSTGRES_USER', 'restaurant'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'restaurant'),
        'HOST': env.str('DB_HOST', 'postgres'),
        # 'HOST': env.str('DB_HOST', 'localhost'),
        'PORT': env.int('DB_PORT', 5432),
    }
}
