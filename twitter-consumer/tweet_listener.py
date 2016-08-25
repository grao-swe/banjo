import tweepy
import json

from message_broker_send import Sender
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


__author__ = "grao-swe"

consumer_key = "Ubq2t02m1orHdmm19FOKJnNrs"
consumer_secret = "PsdMttRUrCvahpUX1cb1K1BlWjWbtd4Cp0SOThjzJe0VO6Oj2F"

access_token = "763950174376894464-f9iwOpbKBtUyVRAmFM1bQSw7YQZVUVx"
access_token_secret = "2SvlBAKdeySxDsBx8bWkmSOp4VprUleGmzg0sAgb9yWwv"

sentiment_keywords = ["active", "alert", "excited", "elasted", "happy", "pleasant", "content", "serene",
                      "relaxed", "calm", "subdued", "bored", "depressed", "unhappy", "sad", "unpleasant",
                      "upset", "stressed", "nervous", "tense"]

class TweetListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    sender = None
    
    def __init__(self):
        self.sender = Sender("geo-tweet")
    
        
    def on_data(self, data):
        try:
            tweet_json = json.loads(data)
            coordinates = tweet_json.get('coordinates')
            place = tweet_json.get('place')
            if coordinates and coordinates.get('coordinates'):                                
                tweet = {                         
                         "coordinates": coordinates.get("coordinates"),
                         "text": tweet_json.get("text")
                         }                                
                self.sender.send(json.dumps(tweet)) 
#             if place: 
#                 tweet = {
#                          "text": tweet_json.get("text"),
#                          "coordinates": place
#                          }
#                 self.sender.send(json.dumps(tweet))
        except json.JSONDecoder:
            # (TODO) error log the tweet with error
            print "ERROR: Can't decode {}".format(data)
        except Exception as e:
            print "ERROR: Can't send: {}".format(data)
        return True
        

    def on_error(self, status):
        print(status)
        
    def on_disconnect(self, notice):
        self.sender.close()
        return StreamListener.on_disconnect(self, notice)


if __name__ == '__main__':
    
    l = TweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=sentiment_keywords, async=True)
    
#     stream.filter(locations=[-122.75,36.8,-121.75,37.8])
    
    
    
    
