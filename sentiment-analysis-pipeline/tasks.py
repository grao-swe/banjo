import json

from textblob import TextBlob
from celery import Celery
from mongodb_insert_client import SentimentMongoDBInsertClient

app = Celery("tasks", broker="amqp://guest@localhost//")

mongodb = SentimentMongoDBInsertClient('localhost', 27017, 'geo_tweet', 'sentiments')

@app.task
def analyze(body):
    """
    Analyzes the text and returns a dictionary of text with its sentiment polarity and coordinates.
    """
    try:
        tweet_json = json.loads(body)
        text = tweet_json.get("text")
        coordinates = tweet_json.get("coordinates")
        
        tb = TextBlob(text)
        polarity = tb.sentiment.polarity,

        document = {
                "text": text,
                "polarity": polarity,
                "coordinates": coordinates
                }
        mongodb.insert(document)
    
    except json.JSONDecoder:
        #(TODO) log error
        print "ERROR: Can't decode {}".format(body)
    except Exception as e:
        print "ERROR: Error {} while analyzing body: {}".format(e, body)







