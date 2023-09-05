import requests
import json
import allure
from typing import List, Dict, Union, Optional

from api_objects.api_base import APIBase
from Util.compare import is_numeric_value_met_condition

star_wars_base_url = 'https://swapi.py4e.com/api'

class VehiclesAPI(APIBase):
    PATH = 'vehicles/'
    def __init__(self,session):
        super().__init__(session, self.PATH)
        
    @allure.step("Filter vehicles") 
    def filter_vehicles_by_numeric_attribute(self, attribute_name: str, compare_type: str, require_value: Union[int, float]
    ) -> List[Dict[str, Union[int, float]]]:
        filter_vehicles = []
        for vehicle in self.results_data: 
            if isinstance(require_value, (int, float)) and vehicle[attribute_name] == "unknown":
                continue
            if is_numeric_value_met_condition(vehicle[attribute_name], compare_type, require_value):
               filter_vehicles.append(vehicle)     

        filter_vehicles_list = [{vehicle['name']: vehicle[attribute_name]} for vehicle in filter_vehicles]
        return filter_vehicles_list

