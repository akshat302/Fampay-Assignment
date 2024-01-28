import os
from celery import Celery
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Youtube_Search.settings')
  
celery_app = Celery('Youtube_Search')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'fetch_video_data': {
        'task': 'search_backend.tasks.fetch_video_data',
        'schedule': 30.0  # It will run every 30 seconds
    }
}