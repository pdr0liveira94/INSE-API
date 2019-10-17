"""This module will serve the api request."""
from config import client
from flask import request, jsonify
from service import 

# Import the helpers module
helper_module = imp.load_source('*', './Api/app/helpers.py')

@app.route('/', methods=['GET'])
def mainPage():
    return jsonify({"message": "I'm alive."})

@app.route('/answer', methods=['GET'])
def get_videos():
    try:
        # Retrieve url data
        query_params = helper_module.parse_query_params(request.query_string)

        if (query_params not None and
            'id' in query_params):
            details = query_params

            return response, 200
        else:
            return "Missing Parameter", 400
    except Exception as e:
        print(e)
        return "Server Error", 500

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
