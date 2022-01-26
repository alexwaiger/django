import os, sys
sys.path.append('/home/boss/www/top10casino-au-com/django/top10casino-au-com')
os.environ['DJANGO_SETTINGS_MODULE'] = 'top10casino-au-com.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()