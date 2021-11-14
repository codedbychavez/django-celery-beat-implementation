from __future__ import absolute_import
import os
import sys
import requests
from datetime import datetime

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


@app.task(bind=True)
def second_task(self):
    print('second task!')


@app.task(bind=True)
def trigger_workflow(self):
    myFile = open('/Users/chavez/Desktop/Creative Work/repos/django-celery-beat-implementation/djbeat/cron_log.txt', 'a') 
    myFile.write('\nAccessed on ' + str(datetime.now()))
    pload = {
        'workflow':3,
        'body':"\"{\\\"to\\\":\\\"chavez.harris@v75inc.com\\\",\\\"from\\\":\\\"chavez.harris@v75inc.com\\\",\\\"subject\\\":\\\"Foo\\\",\\\"body\\\":\\\"Hello World!\\\"}\""
        }
    r = requests.post('https://localhost:8000/api/v1/workflow/workflow_trigger/',data=pload, verify=False)
    print(r.text)
