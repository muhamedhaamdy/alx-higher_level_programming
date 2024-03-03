#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response'''
import requests
import sys


r = requests.get(sys.argv[1])
code = r.status_code
if code >= 400:
    print('Error code:', code)
else:
    print(r.text)
