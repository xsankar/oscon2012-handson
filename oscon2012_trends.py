#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth
#
# Get Trending Topics
#
# http://api.twitter.com/1/trends/:woeid.format
# woeid=1 = global
# https://dev.twitter.com/docs/api/1/get/trends/%3Awoeid
# http://engineering.twitter.com/2010/02/woeids-in-twitters-trends.html
# https://dev.twitter.com/blog/changing-trends-api
# https://dev.twitter.com/docs/api/1/get/trends/available
# Get available trends
# For a day
url = 'http://api.twitter.com/1/trends/daily.json'
payload={"date":"2012-07-07"}
r = requests.get(url, params=payload)
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
#
'''
url = 'http://api.twitter.com/trends/available.json'
r = requests.get(url)
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
#
url='http://api.twitter.com/1/trends/1.json'
r = requests.get(url)
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
'''
