import os
import json
import logging

class APIBase:
    def __init__(self, session, path=""):
        base_url = os.getenv("API_DOMAIN")
        self.session = session
        self.url = f'{base_url}{path}'
        self.response = None
        self.json_body = None

    def api_request(self, method, **kwargs):
        request_info = f'Request mehod: {method}\n Request URL: {self.url}'
        logging.info(request_info)

        self.response = self.session.request(method, self.url, **kwargs)
        logging.info(f'Response status: {self.get_response_status()}')
        
        self.get_response_data()
        

    def get_response_status(self):
        return self.response.status_code    

    def get_response_data(self):
        try: 
            self.json_body = self.response.json()
            pretty_json = json.dumps(self.json_body, indent=4)
            logging.debug(f"Response Data: {pretty_json}")
            
        except Exception as e:
            logging.info(f"Exception: {e}")
            logging.debug("Response: No Response Body")

  
