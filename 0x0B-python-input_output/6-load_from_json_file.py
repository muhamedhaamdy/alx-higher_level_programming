#!/usr/bin/python3
"""the begining of the file"""
import json


def load_from_json_file(filename):
    """save a json representation to a file"""
    with open(filename, 'r') as f:
        return json.load(f)
