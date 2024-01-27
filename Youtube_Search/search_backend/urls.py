from django.urls import path
from .views import VideoDataListView, VideoResults, SearchVideView

urlpatterns = [
    # path('get_video_result/', VideoResults.as_view(), name='video_result'),
    path('get_videos_list/', VideoDataListView.as_view(), name='videos_list'),
    path('get_videos_list_by_query/', SearchVideView.as_view(), name='search_video')
]

