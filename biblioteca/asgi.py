"""
ASGI config para projeto biblioteca.
Ele expõe o ASGI callable como uma variável de nível de módulo chamada ''application''.
Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')

application = get_asgi_application()