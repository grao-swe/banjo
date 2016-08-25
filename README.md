
# banjo


# twitter-listener

The twitter listener is created inheriting tweepy.streaming.SteamListener 
and set of sentiment keywords. The listener filters tweets based on the
keywords and sends it to the RabbitMQ sender.

# sentiment-analysis
The RabbitMQ receiver that receives the tweets coming in and sends to the 
Celery worker.

The Celery worker takes the data and stores that into the MongoDB. 

# sentiment-rest-api

The Flask application running on http://127.0.0.1:5000/ listens to the 
rest api request at /sentiment endpoint. The request requires 3 query 
params - lat, lng, rad which is the latitude, longitude and radius (in 
miles) respectively. This endpoint either returns the result, for example,

{
    "average_polarity": 0.2525, 
    "most_negative": {
        "coordinates": [
            -98.309, 
            56.9547
        ], 
        "text": "Trend Alert: #TFCLive. More trends at https://t.co/SHjd3tkINE #trndnl https://t.co/sxeKuvTjo0"
    }, 
    "most_positive": {
        "coordinates": [
            -95.9113815, 
            41.1410142
        ], 
        "text": "A customer brought her copy of Firefly in to play. She didn't realize her dad got bored one day\u2026 https://t.co/52qVI6X7Gz"
    }, 
    "tweets": 14
}

or the error message if the query params not proper, for example,

{
    "message": "Provide lng(longitude), lat(latitude), rad(radius in miles) as query params to use this Sentiment API"
}

