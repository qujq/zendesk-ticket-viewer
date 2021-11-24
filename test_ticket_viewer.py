import json
import unittest
from ticket_viewer import app

app.testing = True

class TestTicketViewer(unittest.TestCase):
    def test_get_ticket(self):
        with app.test_client() as client:
            with open('usernamePassword.json', 'r') as f:
                usernameAndPassword = json.load(f)
                USER = usernameAndPassword["username"]
                PWD = usernameAndPassword["password"]
                print(USER, PWD)
                response = client.get("/getTicket?user=" + USER + "&pwd=" + PWD)
                print(response.data)
                assert response.status_code == 200
                assert "tickets" in str(response.data) and "count" in str(response.data)
              