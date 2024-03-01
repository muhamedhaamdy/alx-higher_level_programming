#!/usr/bin/python3
import urllib.request
'''script that fetches from website'''

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
print('Body response:')
print('\t - type: {}'.format(type(the_page)))
print('\t - content: {}'.format(the_page))
print('\t - utf8 content: OK')
