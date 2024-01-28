from django.db import models
from djongo import models as djongo_models

# Create your models here.
class VideoData(djongo_models.Model):
    title = djongo_models.CharField(max_length=128, blank=True)
    description = djongo_models.TextField(blank=True)
    thumbnail_url = djongo_models.URLField()
    publish_datetime = djongo_models.DateTimeField()
    video_id = djongo_models.CharField(max_length=128, unique=True)
    created_at = djongo_models.DateTimeField(auto_now_add=True)
