"""
Configuració WSGI del projecte MY_SITE.

Aquest fitxer exposa l'aplicació WSGI utilitzada per desplegar
el projecte Django en un servidor web.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MY_SITE.settings')

application = get_wsgi_application()
