import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pesez.settings')

app = Celery('colon_toothbrush',
             include=['pesez.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()