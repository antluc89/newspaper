import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'mailing': {
        'tasks': 'news.tasks.weekly_send_mail_task',
        'schedule': crontab(minute='00', hour='8', day_of_week='monday'),
        'args': ()
    }
}
