from rest_framework import serializers
from .models import VideoData

class VideoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoData
        fields = '__all__'

    def create(self, validated_data):
        video_data = VideoData.objects.create(**validated_data)
        video_data.save()
        return video_data