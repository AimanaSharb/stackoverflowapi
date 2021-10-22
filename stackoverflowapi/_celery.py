import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackoverflowapi.settings')

app = Celery('stackoverflowapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Почему redis быстрее postgres?
# postgres работает на жестком диске
# redis работает на нашей оперативной памяти


app.conf.beat_schedule = {
    'add-eve'
}
