from pymongo import MongoClient, GEO2D


class SentimentMongoDBInsertClient(MongoClient):
    
    client = None
    db = None
    collection = None
    
    def __init__(self, host, port, db, collection):        
        self.client = MongoClient(host, port)
        self.db = getattr(self.client, db)
        self.collection = getattr(self.db, collection)
        
    def insert(self, document):
        self.collection.insert_one(document)
        
if __name__ == "__main__":

    host = "localhost"
    db = "geo_tweet"
    collection = "sentiments"

    mongodb = SentimentMongoDBInsertClient(host, 27017, db, collection)
    
    document1 = {
                 'polarity': (0.8,), 
                 'text': u'Happy Birthday To ME\U0001f44f\U0001f3fb\U0001f389\U0001f389\U0001f389\U0001f490\U0001f388 @ Oak Bluffs, Massachusetts https://t.co/Y4tAOvOhrP', 
                 'coordinates': [-70.5625, 41.45416667]
                 }
    document2 = {
                 'polarity': (0.68,),
                 "text": "when you are happy loving yourself, you can truly be happy loving someone else just as much.\\u2026 https://t.co/QPg48tpEQd", 
                 "coordinates": [-75.17175579, 39.9496614]
                 }
     
    mongodb.insert(document1)
    mongodb.insert(document2)

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        