__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MountainHacks.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
