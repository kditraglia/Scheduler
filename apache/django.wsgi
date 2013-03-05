import os, sys
import django.core.handlers.wsgi

sys.path.append('/home/kevin/Projects/Scheduler')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Scheduler.settings'
application = django.core.handlers.wsgi.WSGIHandler()
