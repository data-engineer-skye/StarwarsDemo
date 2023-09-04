import pytest
import allure
import logging

from api_objects.vehicles_api import VehiclesAPI


@allure.feature("Vehicles")
@allure.story("Please find out all vehicles which max_atmosphering_speed is over 1000.")
def test_get_all_vehicles_max_atmosphering_speed_over_1000(session):
    with allure.step("Get all vehicles data"):
        vehicles_api_obj = VehiclesAPI(session)
        vehicles_api_obj.get_vehicles_data()
        assert vehicles_api_obj.get_response_status() == 200

    expect_result = [{'T-16 skyhopper': '1200'}, {'TIE/LN starfighter': '1200'}, {'Storm IV Twin-Pod cloud car': '1500'}, {'TIE/IN interceptor': '1250'}, {'Vulture Droid': '1200'}, {'Geonosian starfighter': '20000'}, {'Droid tri-fighter': '1180'}]
    
    with allure.step("Get max_atmosphering_speed > 1000 vehicles"):
        filter_vehicles = vehicles_api_obj.filter_vehicles_by_numeric_attribute("max_atmosphering_speed", "over", 1000)
        logging.info(f'Result: {filter_vehicles}')
        assert filter_vehicles == expect_result

    