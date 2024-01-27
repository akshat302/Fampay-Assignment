import json
import requests
from Youtube_Search.celery import celery_app
from datetime import datetime, timedelta
from .serializers import VideoDataSerializer
from .models import VideoData
from .constants import YOUTUBE_SEARCH_URL, SEARCH_QUERY, API_KEY_LIST, MAX_RESULTS_PER_CALL

@celery_app.task
def fetch_video_data():
    
    if len(API_KEY_LIST) == 0:
        print("All API keys exhausted, need to add new keys")
        return 
    
    current_datetime = datetime.utcnow()
    published_after = current_datetime - timedelta(hours=2)
    published_after_iso_formatted = published_after.isoformat("T") + 'Z'
    key = API_KEY_LIST[-1]
    search_params = {
        "part": "snippet",
        "type": "video",
        "publishedAfter": published_after_iso_formatted,
        "q": SEARCH_QUERY,
        "key": key,
        "maxResults": MAX_RESULTS_PER_CALL
    }
    try:
        response = save_video_data(search_params)
        print(response)
    except Exception as e:
        exhausted_key = API_KEY_LIST.pop()
        print(f"the API key {exhausted_key} got exhausted, using next available key")
        new_key = API_KEY_LIST[-1]

        search_params["key"] = new_key
        response = save_video_data(new_key)
        print(response)

def save_video_data(search_params):

    response = requests.get(YOUTUBE_SEARCH_URL, params=search_params)
    data = json.loads(response.text)
    videos_data = data.get('items', [])
    for video in videos_data:
        video_data_dict = {
                "title":video["snippet"]["title"],
                "description" : video["snippet"]["description"],
                "thumbnail_url" : video["snippet"]["thumbnails"]["default"]["url"],
                "publish_datetime" : video["snippet"]["publishedAt"],
                "video_id" : video["id"]["videoId"]}
        existing_video = VideoData.objects.filter(video_id=video_data_dict['video_id']).first()
        if not existing_video:
            video_data_serializer = VideoDataSerializer(data=video_data_dict)
            if video_data_serializer.is_valid():
                video_data = video_data_serializer.save()
                return {"status": "SUCESS", "message": "vide data saved successfully to db", "data": video_data}
            else:
                return {"status": "FAILED", "message": f"Some error occured while saving video data to db: {video_data_serializer.errors}"}
        else:
            return {"status": "FAILED", "message": f"The Video with the video id {video['id']['videoId']}  already exists in the db"}