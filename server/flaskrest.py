import logging
from flask import Flask, jsonify, request
import requests
from flask_restful import Api, Resource
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
api = Api(app)

# Set up logging to provide debug information
logging.basicConfig(level=logging.DEBUG)

# Define the Marshmallow schema for validation and serialization
class CatImageSchema(Schema):
    id = fields.Str(required=True)
    url = fields.Str(required=True)
    width = fields.Int(required=True)

# Instantiate the schema
# Handle multiple results (GET: [ {}, {} ])
cat_image_schema = CatImageSchema(many=True)
# Handle a single object (POST/PUT/PATCH: {})
single_cat_image_schema = CatImageSchema()

# Creating the CatImages resource
class CatImages(Resource):
    def get(self):
        api_url = 'https://api.thecatapi.com/v1/images/search?limit=10'
        
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()  # Get the JSON data from the response
            # print(data)
            # Serialize the data
            serialized_data = cat_image_schema.dump(data)
            return jsonify(serialized_data)
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP error, extracting the status code and error message
            return jsonify({"error": str(http_err)}), 500  # Change to a specific status if necessary
        except Exception as err:
            # Handle other errors
            return jsonify({"error": str(err)}), 500
        
    def post(self):
        try:
            # get incoming JSON DATA , deserializing , validate incoming JSON data
            # .get_json, get_data()
            data = request.get_json()
            # validating data as per schema using Marshmallow 
            # deserializing one object 
            validate_data = single_cat_image_schema.load(data)
            # here you can process or save the validated data as needed 
            
            # SERIALIZING BACK TO JSON 
            serialized_data = single_cat_image_schema.dump(validate_data)
            return jsonify(serialized_data) 
        except ValidationError as ve:
            return jsonify({"errors": ve.messages})
        except Exception as err:
            return jsonify({"error" : str(err)})

# Associate the CatImages resource with the '/cat-images' route
api.add_resource(CatImages, '/cat-images', endpoint='cat-images')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
