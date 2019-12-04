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

        # Retrieving arguments
        name = request.args.get('name')
        id = request.args.get('id')

        branch = request.args.get('branch')
        if branch is not None:
            branch = branch.replace('_', ' ')

        state = request.args.get('state')
        if state is not None:
            state = state.replace('_', ' ')

        city = request.args.get('city')
        if city is not None:
            city.replace('_', ' ')

        # if query_params is not None:        
        if name is not None:
            print('Retrieving an ID')
            result = svc.get_enterprise_id_by_name(name)
            return jsonify({"id": result}), 200

        elif id is not None:
            print('Retrieving an ENTERPRISE')
            result = svc.get_enterprise_by_id(id)
            return  jsonify(result), 200
        
        elif branch is not None or state is not None or city is not None:
            print('Retrieving an collection of ENTERPRISES')

            result = svc.get_enterprises_with_filters(branch, state, city)
            return jsonify(result), 200
        else:
            result = svc.get_enterprises()
            return jsonify(result), 200
    except Exception as e:
        print(e)
        return "Server error", 500

@app.route('/branches', methods=['GET'])
def get_branches():
    try:
        return jsonify(svc.get_branches()), 200
    except:
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
