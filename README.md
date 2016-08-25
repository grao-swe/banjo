
# banjo


# twitter-listener

The twitter listener is created inheriting tweepy.streaming.SteamListener 
and set of sentiment keywords. The listener filters tweets based on the
keywords and sends it to the message broker queue using the sender. 
