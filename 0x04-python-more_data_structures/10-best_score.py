#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    maximum_value = max(a_dictionary.values())
    first_key = None

    for key, value in a_dictionary.items():
        if value == maximum_value:
            first_key = key
            break

    return first_key
