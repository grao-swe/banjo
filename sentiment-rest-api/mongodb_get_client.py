from pymongo import MongoClient, GEO2D


class SentimentMongoDBGetClient(MongoClient):
    
    client = None
    db = None
    collection = None
    
    def __init__(self, host, port, db, collection):        
        self.client = MongoClient(host, port)
        self.db = getattr(self.client, db)
        self.collection = getattr(self.db, collection)
    
    def find_within_radius(self, coordinates, radius):
        if len(coordinates) != 2:
            raise ValueError("ERROR: Invalid coordinates. Must be [lng, lat]")
        if not isinstance(radius, (float, int)) or radius < 0:
            raise ValueError("ERROR: Invalid radius. Must be greater than 0.")
        
        query = {
                 "coordinates": {
                               "$within" : {
                                             "$center": [coordinates, radius]
                                             }
                               }
                 }
        
        cursor = self.collection.find(query)        
        if cursor:
            return [document for document in cursor]            
        return []   
        
        
if __name__ == "__main__":
    # Test

    mongodb = SentimentMongoDBGetClient("localhost", 27017)
    mongodb.set_db("geo_tweet")
    mongodb.set_collection("sentiments")
    
    results = mongodb.find_within_radius([107.5625, -5.45416667], 5)
    for res in results:
        print res
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        