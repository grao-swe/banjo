from flask import Flask, request
from flask_restful import Resource, Api
from mongodb_get_client import SentimentMongoDBGetClient

app = Flask(__name__)
api = Api(app)

mongodb = SentimentMongoDBGetClient("localhost", 27017, "geo_tweet", "sentiments")


class GeoSentiment(Resource):
    
    def average_sentiment(self, coordinates, radius):
        results = mongodb.find_within_radius(coordinates, radius)
        if results:
            count = len(results)
            most_positive = {"polarity": -1.0}
            most_negative = {"polarity": 1.0}
            total = 0.0
            
            for res in results:
                text = res.get('text')
                polarity = res.get('polarity')[0]
                total += polarity
                if most_positive.get("polarity") < polarity:
                    most_positive = res
                if most_negative.get("polarity") > polarity:
                    most_negative = res                
            avg = total/count
            return {
                    "tweets": count,
                    "average_polarity": avg,
                    "most_positive": {
                                      "text": most_positive.get("text"),
                                      "coordinates": most_positive.get("coordinates")
                                      },
                    "most_negative": {
                                      "text": most_negative.get("text"),
                                      "coordinates": most_negative.get("coordinates")
                                      }
                    }
        else:
            return {
                    "status": 404,
                    "error": "Not results found matching query."
                    }
    
    def get(self):        
        
        try:
            lat = float(request.args.get('lat'))
            lng = float(request.args.get('lng'))
            rad = float(request.args.get('rad'))
        except ValueError:
            return {"error": "Invalid params. Must be float."}
        except TypeError:
            return {"message": "Provide lng(longitude), lat(latitude), rad(radius in miles) as query params to use this Sentiment API"}
        
        print lat, lng, rad
        
        if all([lat, lng, rad]):
            return self.average_sentiment([lng, lat], rad)            
        else:
            return {"message": "Provide lng(longitude), lat(latitude), rad(radius in miles) as query params to use this Sentiment API"}
            
        
api.add_resource(GeoSentiment, '/sentiment/', endpoint='sentiment')

if __name__ == "__main__":
    
    app.run(debug=True)
