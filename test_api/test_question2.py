import pytest
import allure
import logging

from api_objects.films_api import FilmsAPI

@allure.feature("Films")
@allure.story("Please list all the film names and sort the name by episode_id.")
def test_get_sorted_films_name(session):
    with allure.step("Get all films data"):
        films_api_obj = FilmsAPI(session)
        films_api_obj.get_films_data()
        assert films_api_obj.get_response_status() == 200

    expect_films_count = films_api_obj.json_body['count']
    expect_films_list = ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Force Awakens']
    
    with allure.step("List all the film names sorted by episode_id"):
        sorted_films_name = films_api_obj.get_films_name_sorted()
        assert len(sorted_films_name) == expect_films_count

        logging.info(f'Result: {sorted_films_name}')
        assert sorted_films_name == expect_films_list