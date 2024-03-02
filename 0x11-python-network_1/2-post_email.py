#!/usr/bin/python3
'''sends a POST request to the passed URL'''
import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    email = {}
    url = sys.argv[1]
    email['email'] = sys.argv[2]

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page)
