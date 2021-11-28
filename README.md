# Zendesk-ticket-viewer

### Usage
#### 1. Environment
Python version 3.8

Requirements are listed in requirements.txt, install them with command:

```Shell
pip install -r requirements.txt
```
#### 2. Quick start

First, filling ```config.json``` with subdomain, username and password. Enable API password access in Zendesk Admin Center. Example:

```Json
// config.json
{
    "username": "user@example.com",
    "password": "myPassword",
    "subdomain": "https://zccMySubdomain.zendesk.com"
}
```

Start Flask server:

```Shell
python3 ticket_viewer.py
```

The webpage url is http://127.0.0.1:8000/

Run unittest:
```Shell
python3 -m unittest test_ticket_viewer.py
```

### Features

List all ticket subjects and paginate into 25 items per page.

Support go to next page or previous page of tickets list

Display requester name, subject, description for each ticket by clicking subject of tickets in the list.

Handle authentication errors, API unavailable and other errors by showing error information on webpage.

Contains unit test for ticket requesting and parsing

### Why Flask?
This project is not a complicated project and features are direct. So, I want to make it easier to run and use. If I totally separate front end and back end, for example, use React in front end and Nodejs in back end. There will be more libraries to install and more steps to run such a project with simple features. Also, with pip tools, required libraries are easy to install by just one command. To make everything easy, I choose Flask.
