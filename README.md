# Fampay-Assignment

Assignment Link - https://fampay.notion.site/fampay/Backend-Assignment-FamPay-32aa100dbd8a4479878f174ad8f9d990

### Requirements

- Docker (https://docs.docker.com/engine/install/)

### Steps to run

1. clone the github repo - git clone https://github.com/akshat302/Fampay-Assignment.git
2. cd into the SuperU-Backend folder - cd Fampay-Assignment/Youtube_Search
3. run docker-compose up --build -d

### Entities  

1. VideoData
2. 
### Database Models 

VideoData:

	  title: title of the video
    description: description of the video
    thumbnail_url: url of the thumbnail of the video
    publish_datetime = published datetime of the video
    video_id = unique video id of the video
    created_at = datetime at which entry is created in db

### API Details 

get_videos_list -

    URL - "/get_videos_list/"
    Type - GET
    
    Description: 
      1. Retrieves the list of videos in reverse chronological order of publish datetime in a paginated way. (10 results per page) 
    Response -   {
    "count": 150,
    "next": "http://127.0.0.1:8000/get_videos_list/?page=2",
    "previous": null,
    "results": [
        {
            "id": 157,
            "title": "Australia vs West indies 2nd Test live day 4 2024 🔴LIVE AUS vs WI DAY 4 2024🔴LIVE CRICKET SCORE",
            "description": "Australia vs West indies 2nd Test live day 4 2024 LIVE AUS vs WI DAY 4 2024  LIVE CRICKET SCORE NOTE : ( This is not ...",
            "thumbnail_url": "https://i.ytimg.com/vi/h3153k2Z1F8/default.jpg",
            "publish_datetime": "2024-01-28T08:49:22Z",
            "video_id": "h3153k2Z1F8",
            "created_at": "2024-01-28T09:01:34.986000Z"
        },
        {
            "id": 155,
            "title": "Live 🛑:🏆 33rd Gadadharpur cricket cup 2k24.Grandfinal,gadagharpur,cuttack#ak143",
            "description": "",
            "thumbnail_url": "https://i.ytimg.com/vi/OICgC5x1EjU/default.jpg",
            "publish_datetime": "2024-01-28T08:42:35Z",
            "video_id": "OICgC5x1EjU",
            "created_at": "2024-01-28T09:01:34.527000Z"
        }
      }

get_videos_list_by_query - 
    
    URL - "/get_videos_list_by_query/"
    Type - GET
    Query Params - {
          query : "jadeja"
          }
    Description :
      1. Retrieves the list of videos based on search query on title and description in reverse chronological order of publish datetime  
      2. It implements a partial match for search query on tile and description

    Response - {
                  "count": 2,
                  "next": null,
                  "previous": null,
                  "results": [
                      {
                          "id": 79,
                          "title": "Jadeja Rahul and Jaiswal great Performance #shorts #youtubeshorts #cricket #klrahul #ravindrajadeja",
                          "description": "Jadeja Rahul and Jaiswal great Performance #shorts #youtubeshorts #cricket #klrahul #ravindrajadeja Ind vs England,Ind Vs ...",
                          "thumbnail_url": "https://i.ytimg.com/vi/8UCYOV5fINE/default.jpg",
                          "publish_datetime": "2024-01-27T15:00:06Z",
                          "video_id": "8UCYOV5fINE",
                          "created_at": "2024-01-27T15:37:37.857000Z"
                      },
                      {
                          "id": 36,
                          "title": "Ollie Pope Century Gives England Hope | Hyderabad | Day 3 | IND VS ENG",
                          "description": "0:00 INTRO 2:54 THANKS TO HELL ENERGY 4:00 OLLIE POPE'S INNINGS 7:31 JADEJA BEATS EVERYONES BAT 10:46 ARE ...",
                          "thumbnail_url": "https://i.ytimg.com/vi/ECtxTtk2PYw/default.jpg",
                          "publish_datetime": "2024-01-27T12:34:52Z",
                          "video_id": "ECtxTtk2PYw",
                          "created_at": "2024-01-27T14:54:59.874000Z"
                      }
                }
