import os
import json
import logging
import allure
from typing import Any, Dict

class APIBase:
    def __init__(self, session, path=""):
        base_url = os.getenv("API_DOMAIN")
        self.session = session
        self.url = f'{base_url}{path}'
        self.response = None
        self.json_body = None
        self.results_data = []

    def api_request(self, method: str, **kwargs: Dict[str, Any]) -> None:
        request_info = f'Request mehod: {method}, Request URL: {self.url}'
        logging.info(request_info)

        self.response = self.session.request(method, self.url, **kwargs)
        logging.info(f'Response status: {self.get_response_status()}')
        
        self.get_response_data()        

    def get_response_status(self) -> int:
        return self.response.status_code    

    def get_response_data(self):
        try: 
            self.json_body = self.response.json()
            pretty_json = json.dumps(self.json_body, indent=4)
            logging.debug(f"Response Data: {pretty_json}")
            
        except Exception as e:
            logging.info(f"Exception: {e}")
            logging.debug("Response: No Response Body")

    @allure.step("Get resource all data") 
    def get_all_data(self):
        next_page = True
        results_data = []

        while next_page:
            self.api_request("get")     
            results_data += self.json_body['results']
            next_page = self.json_body['next']
            self.url = next_page
        self.results_data += results_data         

    @allure.step("Get resource by id") 
    def get_data_by_id(self, resource_id) -> None:
        self.url += f'{resource_id}/'
        self.api_request("get")     

  
