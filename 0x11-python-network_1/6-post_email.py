#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL'''
import requests
import sys


if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=email)
    print(r.text)
