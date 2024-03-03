#!/usr/bin/python3
'''sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter'''
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ''
    else:
        q = sys.argv[1]
    info = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=info)
    try:
        res = r.json()
        if not res:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name'))
    except ValueError:
        print('Not a valid JSON')
