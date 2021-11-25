import json
import unittest
from ticket_viewer import app

app.testing = True

class TestTicketViewer(unittest.TestCase):
    def test_get_ticket(self):
        with app.test_client() as client:
            with open('usernamePassword.json', 'r') as f:
                usernameAndPassword = json.load(f)
                username = usernameAndPassword["username"]
                password = usernameAndPassword["password"]
                response = client.get("/getTicket?user=" + username + "&pwd=" + password)
                response_data = json.loads(response.data)
                assert response.status_code == 200
                assert "tickets" in response_data.keys() and "count" in response_data.keys()
              