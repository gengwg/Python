#!/usr/bin/env python

"""
print the redirect path of a url.

e.g.:
$ py url_redirect.py
Request was redirected
301 http://google.com/
Final destination:
200 http://www.google.com/
"""

import requests

someurl = 'http://google.com'
response = requests.get(someurl)

if response.history:
    print "Request was redirected"
    for resp in response.history:
        print resp.status_code, resp.url
    print "Final destination:"
    print response.status_code, response.url
else:
    print "Request was not redirected"
