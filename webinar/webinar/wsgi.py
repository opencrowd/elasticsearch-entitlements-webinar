# 2014.06.03 13:21:06 EDT
"""
WSGI config for webinar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webinar.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.06.03 13:21:06 EDT
