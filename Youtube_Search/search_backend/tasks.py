import json
import requests
from Youtube_Search.celery import celery_app
from datetime import datetime, timedelta
from .serializers import VideoDataSerializer
from .models import VideoData
from .constants import YOUTUBE_SEARCH_URL, SEARCH_QUERY, API_KEY_LIST, MAX_RESULTS_PER_CALL

@celery_app.task
def fetch_video_data():
    
    if not API_KEY_LIST:
        print("All API keys exhausted, need to add new keys")
        return 
    
    current_datetime = datetime.utcnow()
    published_after = current_datetime - timedelta(hours=4)
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

        if not API_KEY_LIST:
            print("All API keys exhausted, need to add new keys")
            return 
        
        new_key = API_KEY_LIST[-1]
        search_params["key"] = new_key
        response = save_video_data(new_key)
        print(response)

def save_video_data(search_params):

    response = requests.get(YOUTUBE_SEARCH_URL, params=search_params)
    data = json.loads(response.text)
    videos_data = data.get('items', [])
    videos_saved_to_db  =[]
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
                videos_saved_to_db.append(video_data_dict)
                print("video data successfully saved to db", video_data_dict)
            else:
                print(f"Some error occured while saving video data to db: {video_data_serializer.errors}")
        else:
            print(f"The Video with the video id {video_data_dict['video_id']}  already exists in the db")
    return {"status": "SUCESS", "message": "video data saved successfully to db", "data": videos_saved_to_db}