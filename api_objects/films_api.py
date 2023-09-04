import requests
import json
import allure

from api_objects.api_base import APIBase


class FilmsAPI(APIBase):
    PATH = 'films/'

    def __init__(self, session):
        super().__init__(session, self.PATH)

    @allure.step("Get Films api data") 
    def get_films_data(self, film_id=None):
        if film_id and isinstance(film_id, int):
            self.url += f'{film_id}/'
        self.api_request("get")          

    @allure.step("Get unique species") 
    def get_unique_species_count(self):
        species_list = self.json_body['species']    
        unique_species_count = len(set(species_list))
        return unique_species_count

    @allure.step("Get films name") 
    def get_films_name_sorted(self):
        films = self.json_body['results']
        sorted_films = sorted(films, key=lambda film: film['episode_id'])
        films_name_list = [film['title'] for film in sorted_films]
        return films_name_list
       