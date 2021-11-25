import json
import unittest
from ticket_viewer import app

app.testing = True

with open('usernamePassword.json', 'r') as f:
    usernameAndPassword = json.load(f)
    username = usernameAndPassword["username"]
    password = usernameAndPassword["password"]

class TestTicketViewer(unittest.TestCase):
    response = ''
    response_data = ''
    def setUp(self):
        with app.test_client() as client: 
            self.response = client.get("/getTicket?user=" + username + "&pwd=" + password)
            self.response_data = json.loads(self.response.data)
    
    def test_get_ticket(self):        
        assert self.response.status_code == 200
        assert "tickets" in self.response_data.keys() and "count" in self.response_data.keys()
    