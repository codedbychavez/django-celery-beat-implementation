from __future__ import absolute_import
import os
import sys

from celery import Celery
import django

app = Celery('djbeat')

app.config_from_object('django.conf:settings', namespace='CELERY')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djbeat.settings')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../djbeat')))
django.setup()
from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def print_hello(self):
    print('Hello World!')
