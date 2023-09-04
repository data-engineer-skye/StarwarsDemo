import requests
import json
import allure

from api_objects.api_base import APIBase
from Util.compare import is_numeric_value_met_condition

star_wars_base_url = 'https://swapi.py4e.com/api'

class VehiclesAPI(APIBase):
    PATH = 'vehicles/'
    def __init__(self,session):
        super().__init__(session, self.PATH)

    @allure.step("Get vehicles api data") 
    def get_vehicles_data(self, vehicle_id=None):
        next_page = True
        results_data = []

        if vehicle_id and isinstance(vehicle_id, int): 
            self.url += f'{vehicle_id}/'
            next_page = False
        
        while next_page:
            self.api_request("get")     
            results_data += self.json_body['results']
            next_page = self.json_body['next']
            self.url = next_page
        self.results_data = results_data
        
    @allure.step("Filter vehicles") 
    def filter_vehicles_by_numeric_attribute(self, attribute_name, compare_type, require_value):
        filter_vehicles = []
        for vehicle in self.results_data: 
            if isinstance(require_value, (int, float)) and vehicle[attribute_name] == "unknown":
                continue
            if is_numeric_value_met_condition(vehicle[attribute_name], compare_type, require_value):
               filter_vehicles.append(vehicle)     

        filter_vehicles_list = [{vehicle['name']: vehicle[attribute_name]} for vehicle in filter_vehicles]
        return filter_vehicles_list

