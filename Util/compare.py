def is_numeric_value_met_condition(value, compare_type, require_value):
    compare_dict = {
        "over": ">",
        "less": "<",
        "equal": "==",
        "greater or equal": ">=",
        "less or equal": "<="
    }    

    result = eval(f"{value} {compare_dict[compare_type]} {require_value}")
    return result