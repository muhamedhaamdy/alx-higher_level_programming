#!/usr/bin/python3
'''sends a request to the URL and displays the value'''
import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
