import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('base.html')

@app.route('/getTicket', methods=["GET"])
def get_ticket():
    url = 'https://zcczendeskcodingchallenge5191.zendesk.com/api/v2/tickets.json?include=comment_count'
    
    # Set default username, password, page index, and page size
    user = USER
    pwd = PWD
    page_index = '1'
    per_page = '25'

    # Set the request parameters
    arg = request.args
    args_data = arg.to_dict()
    if args_data.__contains__("page"): page_index = args_data.get("page")
    if args_data.__contains__("per_page"): per_page = args_data.get("per_page")
    if args_data.__contains__("user"): user = args_data.get("user")
    if args_data.__contains__("pwd"): pwd = args_data.get("pwd")

    # pagination
    url += "&page=" + page_index + "&per_page=" + per_page

    # Do the HTTP get request
    try:
        response = requests.get(url, auth=(user, pwd))
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
    user = USER
    pwd = PWD

    # Set the request parameters
    arg = request.args
    args_data = arg.to_dict()
    user_id = args_data.get("user_id")
    if args_data.__contains__("user"): user = args_data.get("user")
    if args_data.__contains__("pwd"): pwd = args_data.get("pwd")

    url = 'https://zcczendeskcodingchallenge5191.zendesk.com/api/v2/users/'
    url += str(user_id)

    # Do the HTTP get request
    try:
        response = requests.get(url, auth=(user, pwd))
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
    user = USER
    pwd = PWD

    # Set the request parameters
    arg = request.args
    args_data = arg.to_dict()
    ticket_id = args_data.get("ticket_id")
    if args_data.__contains__("user"): user = args_data.get("user")
    if args_data.__contains__("pwd"): pwd = args_data.get("pwd")

    url = 'https://zcczendeskcodingchallenge5191.zendesk.com/api/v2/tickets/'
    url += ticket_id
    
    # Do the HTTP get request
    try:
        response = requests.get(url, auth=(user, pwd))
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

def request_error():
    """
    Handle cases that requests are not made successfully
    """
    response = {"error": "Cannot make request, please check URL"}
    data = jsonify(response)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

if __name__ == '__main__':
    with open('usernamePassword.json', 'r') as f:
        usernameAndPassword = json.load(f)
        USER = usernameAndPassword["username"]
        PWD = usernameAndPassword["password"]
    app.run(host='127.0.0.1', port=8000, debug=True)