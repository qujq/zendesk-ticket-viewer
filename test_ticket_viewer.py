import json
import unittest
from ticket_viewer import app

app.testing = True

class TestTicketViewer(unittest.TestCase):
    response = ''
    response_data = ''
    def setUp(self):
        """
        get ticket list by calling tickets api for further use

        return: 
            response: raw content of response
            response_data: dict type, data part of response
        """
        with app.test_client() as client: 
            self.response = client.get("/getTicket")
            self.response_data = json.loads(self.response.data)
    
    def test_get_ticket(self):  
        """
        test whether get_ticket() function works correctly by
        checking status code and 
        checking keys in response_data dict

        return: N/A
        """      
        assert self.response.status_code == 200, "Status code is not 200"
        assert "tickets" in self.response_data.keys() and "count" in self.response_data.keys(), "Response does not contains one of following keys: tickets, count"
    

    def test_get_selected_ticket(self):
        """
        test whether get_selected_ticket() function works correctly by
        finding a ticket id and call api to get detail of this ticket
        checking response status code
        checking keys

        return: N/A
        """    
        if self.response_data.__contains__("count") and self.response_data["count"] > 0:
            ticket_id = self.response_data["tickets"][0]["id"]
            with app.test_client() as client: 
                selected_ticket_response = client.get("/getSelectedTicket?ticket_id=" + str(ticket_id))
                selected_ticket_response_data = json.loads(selected_ticket_response.data)
                assert selected_ticket_response.status_code == 200, "Status code is not 200"
                assert "ticket" in selected_ticket_response_data.keys(), "Response does not contains key: ticket"

    def test_get_user_name(self):
        """
        test whether get_get_user_name() function works correctly by
        finding a requester id and call api to get detail of this requester
        checking response status code
        checking keys

        return: N/A
        """    
        requester_id = ''
        if self.response_data.__contains__("count") and self.response_data["count"] > 0:
            for i in range(len(self.response_data["tickets"])):
                if(self.response_data["tickets"][i]["requester_id"] != ''):
                    requester_id = self.response_data["tickets"][i]["requester_id"]
                    break

            if requester_id != '':
                with app.test_client() as client: 
                    user_info_response = client.get("/getUserName?user_id=" + str(requester_id))
                    user_info_response_data = json.loads(user_info_response.data)
                    assert user_info_response.status_code == 200, "Status code is not 200"
                    assert "user" in user_info_response_data.keys(), "Response does not contains key: user"