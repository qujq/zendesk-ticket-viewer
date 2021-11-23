import requests
import json
from geolib import geohash
from flask import Flask, request, jsonify

USER = ''
PWD = ''

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('base.html')

@app.route('/getTicket', methods=["GET"])
def get_ticket():
    # Set the request parameters
    url = 'https://zcczendeskcodingchallenge5191.zendesk.com/api/v2/tickets.json?include=comment_count'
    user = USER
    pwd = PWD
    arg = request.args
    page_data = arg.to_dict()
    page_index = page_data.get("page")
    per_page = page_data.get("per_page")
    print(page_index, per_page)
    url += "&page=" + page_index + "&per_page=" + per_page

    # Do the HTTP get request
    response = requests.get(url, auth=(user, pwd))

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
    data = jsonify(data)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

@app.route('/getUserName', methods=["GET"])
def get_user_name():
    # Set the request parameters
    
    arg = request.args
    user_data = arg.to_dict()
    user_id = user_data.get("user_id")
    url = 'https://zcczendeskcodingchallenge5191.zendesk.com/api/v2/users/'
    url += str(user_id)

    # Do the HTTP get request
    response = requests.get(url, auth=(USER, PWD))
    
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
    data = jsonify(data)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

@app.route('/getSelectedTicket', methods=["GET"])
def get_selected_ticket():
    # Set the request parameters

    arg = request.args
    ticket_data = arg.to_dict()
    ticket_id = ticket_data.get("ticket_id")
    url = 'https://zcczendeskcodingchallenge5191.zendesk.com/api/v2/tickets/'
    url += ticket_id

    # Do the HTTP get request
    response = requests.get(url, auth=(USER, PWD))

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
    data = jsonify(data)
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

if __name__ == '__main__':
    with open('usernamePassword.json', 'r') as f:
        usernameAndPassword = json.load(f)
        USER = usernameAndPassword["username"]
        PWD = usernameAndPassword["password"]
    app.run(host='127.0.0.1', port=8000, debug=True)