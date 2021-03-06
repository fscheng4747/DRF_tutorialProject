"""
WSGI config for tutorialProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from dj_static import Cling # 新加入，heroku用

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorialProject.settings')

#application = get_wsgi_application()
application = Cling(get_wsgi_application()) # new change