#!/usr/bin/python3
'''sends a request to the URL and displays the body'''
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            page = res.read()
            page = page.decode('utf-8')
            print(page)
    except urllib.error.HTTPError as err:
        print('Error code: {}"'.format(err.status))
