#!/usr/bin/env python

# oscon2012_open_this_first.py

import requests
import json
from requests.auth import HTTPBasicAuth
#
# To Tect connectivity
#
# GET https://twitter.com/help/test.xml
#
url='https://api.twitter.com/help/test.json'
r = requests.get(url)
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
'''
Sample Output
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "31",
  "content-type": "application/xml; charset=utf-8",
  "date": "Sun, 24 Jun 2012 19:24:58 GMT",
  "etag": "\"648f286e31b9e14af53cbecb69fda62a\"",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sun, 24 Jun 2012 19:24:58 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "k=10.35.102.119.1340565898607981; path=/; expires=Sun, 01-Jul-12 19:24:58 GMT; domain=.twitter.com, guest_id=v1%3A134056589861756165; domain=.twitter.com; path=/; expires=Wed, 25-Jun-2014 07:24:58 GMT, _twitter_sess=BAh7CDoPY3JlYXRlZF9hdGwrCHtF9B84AToHaWQiJWZkOGE0YTgzMTkxNGMx%250ANjY5ZTU5NGQ4MzFlMmU2OGVhIgpmbGFzaElDOidBY3Rpb25Db250cm9sbGVy%250AOjpGbGFzaDo6Rmxhc2hIYXNoewAGOgpAdXNlZHsA--0b7feb394ce9ef4080820a2d2f59e45d780ebf11; domain=.twitter.com; path=/; HttpOnly",
  "status": "200 OK",
  "strict-transport-security": "max-age=631138519",
  "vary": "Accept-Encoding",
  "x-frame-options": "SAMEORIGIN",
  "x-mid": "06858fc242c859f8cca2db3458efe565d2ab28d3",
  "x-runtime": "0.00957",
  "x-transaction": "1eec51a759b45ed1",
  "x-transaction-mask": "a6183ffa5f8ca943ff1b53b5644ef114df9d6bba",
  "x-xss-protection": "1; mode=block"
}
"ok"

'''
