import pytest
import allure
import logging

from api_objects.films_api import FilmsAPI
from Util.compare import assert_check

@allure.feature("Films")
@allure.story("How many different species appears in film-6 (Revenge of the Sith)")
def test_get_unique_species_count_by_film_id(session):
    with allure.step("Get film data by id"):
        films_api_obj = FilmsAPI(session)
        films_api_obj.get_films_data(film_id=6)
        assert_check(films_api_obj.get_response_status(), 200)
    
    with allure.step("Check films title"):
        film_title = films_api_obj.json_body['title']
        assert_check(film_title, "Revenge of the Sith")
    
    with allure.step("Get number of unique species"):
        unique_species_count = films_api_obj.get_unique_species_count()
        logging.info(f'Number of unique species: {unique_species_count}')
        assert_check(unique_species_count, 20)
        

#
