import os, sys
sys.path.append('/home/boss/www/top10casino-au-com/django/main')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()