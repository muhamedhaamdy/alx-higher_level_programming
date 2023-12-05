#!/usr/bin/python3
"""the begining of the file"""
to_json_string = __import__('3-to_json_string').to_json_string


def class_to_json(obj):
    return obj.__dict__
