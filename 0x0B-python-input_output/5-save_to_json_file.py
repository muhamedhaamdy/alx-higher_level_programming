#!/usr/bin/python3
"""the begining of the file"""
import json


def save_to_json_file(my_obj, filename):
    """save a json representation to a file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
