import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('base.html')

@app.route('/getTicket', methods=["GET"])
def get_ticket():
    with open('config.json', 'r') as f:
        config = json.load(f)
        USER = config["username"]
        PWD = config["password"]
        SUBDOMAIN = config["subdomain"]

    url = SUBDOMAIN + '/api/v2/tickets.json?include=comment_count'
    
    # Set default username, password, page index, and page size
    page_index = '1'
    per_page = '25'

    # Set the request parameters
    arg = request.args
    args_data = arg.to_dict()
    if args_data.__contains__("page"): page_index = args_data.get("page")
    if args_data.__contains__("per_page"): per_page = args_data.get("per_page")

    # pagination
    url += "&page=" + page_index + "&per_page=" + per_page

    # Do the HTTP get request
    try:
        response = requests.get(url, auth=(USER, PWD))
    except:
        return request_error()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    data = jsonify(data)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

@app.route('/getUserName', methods=["GET"])
def get_user_name():
    # Set default username and password
    with open('config.json', 'r') as f:
        config = json.load(f)
        USER = config["username"]
        PWD = config["password"]
        SUBDOMAIN = config["subdomain"]

    # Set the request parameters
    arg = request.args
    args_data = arg.to_dict()
    user_id = args_data.get("user_id")

    url = SUBDOMAIN + '/api/v2/users/'
    url += str(user_id)

    # Do the HTTP get request
    try:
        response = requests.get(url, auth=(USER, PWD))
    except:
        return request_error()
    
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    data = jsonify(data)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

@app.route('/getSelectedTicket', methods=["GET"])
def get_selected_ticket():
    # Set default username and password
    with open('config.json', 'r') as f:
        config = json.load(f)
        USER = config["username"]
        PWD = config["password"]
        SUBDOMAIN = config["subdomain"]

    # Set the request parameters
    arg = request.args
    args_data = arg.to_dict()
    ticket_id = args_data.get("ticket_id")

    url = SUBDOMAIN + '/api/v2/tickets/'
    url += ticket_id
    
    # Do the HTTP get request
    try:
        response = requests.get(url, auth=(USER, PWD))
    except:
        return request_error()

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    data = jsonify(data)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

@app.route('/resource', methods = ['POST'])
def update_text():
    print("post---------")
    data = request.form
    print(data)
    print(data.keys())
    print("--------")
    return data

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return app.send_static_file('404.html'), 404

def request_error():
    """
    Handle cases that requests are not made successfully
    """
    response = {"error": "Cannot make request, please check URL"}
    data = jsonify(response)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)