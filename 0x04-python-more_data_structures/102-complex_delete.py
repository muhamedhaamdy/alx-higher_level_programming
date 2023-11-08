#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    key_to_delete = []
    for k, val in a_dictionary.items():
        if val == value:
            key_to_delete.append(k)
    for i in key_to_delete:
        del a_dictionary[i]
    return a_dictionary
