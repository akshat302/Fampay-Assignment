from django.db import models
from djongo import models as djongo_models

# Create your models here.
class VideoData(djongo_models.Model):
    title = djongo_models.CharField(max_length=100)
    description = djongo_models.TextField()
    thumbnail_url = djongo_models.URLField()
    publish_datetime = djongo_models.DateTimeField()
    video_uuid = djongo_models.UUIDField(unique=True)
    created_at = djongo_models.DateTimeField(auto_now_add=True)
