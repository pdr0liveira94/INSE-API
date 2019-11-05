"""This module will serve the api request."""
from flask import request, jsonify
import app.service as svc
from app import app
import imp, json

# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

@app.route('/', methods=['GET'])
def mainPage():
    return jsonify({"message": "I'm alive."})

@app.route('/enterprises', methods=['GET'])
def get_enterprises():
    try:
        query_params = helper_module.parse_query_params(request.query_string)

        if query_params is not None:        
            if 'name' in query_params:
                result = svc.get_enterprise_id_by_name(query_params['name'])
                return jsonify({"id": result}), 200

            elif 'id' in query_params:
                result = svc.get_enterprise_by_id(query_params['id'])
                return  jsonify({"enterprise": result}), 200
            
            else:
                return 'Missing Arguments', 400
    except Exception as e:
        print(e)
        return "Server error", 500

@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
