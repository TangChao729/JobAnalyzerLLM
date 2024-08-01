from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource
from flask_cors import CORS
from marqo_agent import MarqoAgent
from gpt_agent import GPTAgent
import json

# Initialize the Marqo agent
print("Initializing Marqo agent")
DATABASE_PORT = 'http://192.168.31.45:8882'
DATABASE_INDEX = 'kaggle_job_listing'
marqoAgent = MarqoAgent(url=DATABASE_PORT, index=DATABASE_INDEX)
print("Marqo agent initialized")

# Initialize the GPT agent
print("Initializing GPT agent")
gptAgent = GPTAgent()
print("GPT agent initialized")

# Initialize the Flask app
print("Initializing Flask app")
app = Flask(__name__)

# Enable CORS for the Flask app
CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)
print("Flask app initialized")

# TODO: Print out system stats
print("Waiting for requests...")

''' Search endpoint.
Input: JSON object with a query field containing a description of the job listing.
Output: JSON object with the search results.
'''
class Search(Resource):
    def post(self):
        # Get the query from the request
        description = request.get_json().get('query').get('description')

        # Perform search on Marqo index
        try:
            search_results = marqoAgent.search(query=description)
            return Response(json.dumps(search_results), status=200, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({"error": str(e)}), status=500, mimetype='application/json')

''' Compare endpoint.
Input: JSON object with user_info and similar_job_description fields.
Output: JSON object with the response from the GPT agent.
'''
class Compare(Resource):
    def post(self):
        # Get the user_info and similar_job_description from the request
        user_info = request.get_json().get('user_info')
        similar_job_description = request.get_json().get('similar_job_description')

        # Generate response using GPT agent
        try:
            response = gptAgent.generate_response(user_info=user_info, similar_job_description=similar_job_description)
            return jsonify({"response": response})
        except Exception as e:
            return jsonify({"error": str(e)})

# Add the search and compare endpoints to the API
api.add_resource(Search, '/search')
api.add_resource(Compare, '/compare')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)