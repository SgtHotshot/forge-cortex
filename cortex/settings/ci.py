# pylint: disable=unused-wildcard-import, wildcard-import

from .base import *

DATABASES['default'] = {
	'ENGINE':   'django.db.backends.postgresql_psycopg2',
	'NAME':     'cortex_test',
	'USERNAME': 'postgres',
}

