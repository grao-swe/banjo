
# banjo


# twitter-listener

The twitter listener is created inheriting tweepy.streaming.SteamListener 
and set of sentiment keywords. The listener filters tweets based on the
keywords and sends it to the RabbitMQ sender.

#sentiment-analysis
The RabbitMQ receiver that receives the tweets coming in and sends to the 
Celery worker.

The Celery worker takes the data and stores that into the MongoDB. 


