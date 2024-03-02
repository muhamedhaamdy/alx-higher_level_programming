#!/usr/bin/python3
'''script that fetches a website'''
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(r.text)))
print('\t- content: {}'.format(r.text))
