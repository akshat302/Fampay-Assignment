from django.urls import path
from .views import VideoDataListView, SearchVideoView

urlpatterns = [
    path('get_videos_list/', VideoDataListView.as_view(), name='videos_list'),
    path('get_videos_list_by_query/', SearchVideoView.as_view(), name='search_video')
]

