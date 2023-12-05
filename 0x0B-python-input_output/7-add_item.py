#!/usr/bin/python3
"""the begining of the file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    json_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    json_list = []
for av in sys.argv[1:]:
    json_list.append(av)

save_to_json_file(json_list, "add_item.json")
