import requests
import json
import allure
from typing import List

from api_objects.api_base import APIBase


class FilmsAPI(APIBase):
    PATH = 'films/'

    def __init__(self, session):
        super().__init__(session, self.PATH)

    @allure.step("Get unique species") 
    def get_unique_species_count(self) -> int:
        species_list = self.json_body['species']    
        unique_species_count = len(set(species_list))
        return unique_species_count

    @allure.step("Get films name") 
    def get_films_name_sorted(self) -> List[str]:
        films = self.json_body['results']
        sorted_films = sorted(films, key=lambda film: film['episode_id'])
        films_name_list = [film['title'] for film in sorted_films]
        return films_name_list
       