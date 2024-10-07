from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    # define the api route to retrieve data from 
    api_url = 'https://api.thecatapi.com/v1/images/search?limit=10'
    
    try:
        # make a request 
        response = requests.get(api_url)
        # check if the response was successful 
        response.raise_for_status()
        # parse the JSON request 
        data = response.json()
        # empty list 
        serialized_data = []
        # serialize the data to include only specific fields 
        for item in data:
            serialized_data.append({
                "id" : item.get('id'),
                "url" : item.get('url')
            })
        
        # maybe storing data in a db , 
        # return a json response of the data 
        return jsonify(serialized_data), 200
        
    except requests.exceptions.HTTPError as http_err:
        # data modelling 
        return jsonify({"error" : str(http_err)}), response.status_code
    except Exception as err:
        return jsonify({"error" : str(err)}), 500

if __name__ == '__main__':
    app.run(port=5000,debug=True)