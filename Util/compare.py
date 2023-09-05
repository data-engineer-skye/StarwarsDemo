import allure
import logging
from typing import Union

def is_numeric_value_met_condition(value: str, compare_type: str, require_value: Union[int, float]) -> bool:
    """
    Check if a numeric value meets a specified comparison condition.

    Parameters:
    - value: The numeric value to be compared.
    - compare_type: The type of comparison to perform (e.g., 'equal', 'greater', 'less').
    - require_value: The numeric value to compare against.

    Returns:
    - bool: True if the condition is met, False otherwise.

    Raises:
    - ValueError: If an invalid comparison type is provided.
    """

    # Define comparion function
    comparison_functions = {
        "equal": lambda x, y: x == y,
        "greater": lambda x, y: x > y,
        "less": lambda x, y: x < y,
        "greater or equal": lambda x, y: x >= y,
        "less or equal": lambda x, y: x <= y,
        "greater or over": lambda x, y: x >= y,
    }

    if compare_type not in comparison_functions:
        raise ValueError(f"Invalid comparison type: {compare_type}")

    return comparison_functions[compare_type](float(value), require_value)

@allure.step("Check assert")
def assert_check(actual_value, expect_value):
    assert actual_value ==  expect_value, f"Assert Fail, Expect: {expect_value}, but Actual: {actual_value}"  