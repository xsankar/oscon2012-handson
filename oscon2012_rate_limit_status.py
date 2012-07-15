#!/usr/bin/env python

# oscon2012_rate_limit_status.py

import requests
import json
from requests.auth import HTTPBasicAuth
import oscon2012_twitter_utils
client = oscon2012_twitter_utils.get_oauth_client()
#
# To Tect connectivity
#
# GET https://twitter.com/account/rate_limit_status.xml
#
url='https://api.twitter.com/1/account/rate_limit_status.json'
r = requests.get(url) #, auth=HTTPBasicAuth(<username>, password>))
print "========= Anonymous"
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
r = client.get(url) #, auth=HTTPBasicAuth(<username>, password>))
print "======== With OAuth"
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
'''
Sample Output
Anonymous
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "123",
  "content-type": "application/json; charset=utf-8",
  "date": "Sun, 24 Jun 2012 19:32:31 GMT",
  "etag": "\"9a29f14148dada7b421ce7afe93d8b8f\"",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sun, 24 Jun 2012 19:32:31 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "k=10.36.22.125.1340566350993678; path=/; expires=Sun, 01-Jul-12 19:32:30 GMT; domain=.twitter.com, guest_id=v1%3A134056635100282308; domain=.twitter.com; path=/; expires=Wed, 25-Jun-2014 07:32:31 GMT, _twitter_sess=BAh7CDoPY3JlYXRlZF9hdGwrCJss%252Bx84AToHaWQiJWQ0ODNhZWRiMTg2M2Ri%250AZDdkZDkxYzg1YjZiN2Y4MTlhIgpmbGFzaElDOidBY3Rpb25Db250cm9sbGVy%250AOjpGbGFzaDo6Rmxhc2hIYXNoewAGOgpAdXNlZHsA--fe503152d6d0c4157a1a4d633832f08e85902ca4; domain=.twitter.com; path=/; HttpOnly",
  "status": "200 OK",
  "vary": "Accept-Encoding",
  "x-frame-options": "SAMEORIGIN",
  "x-mid": "f63766217716f4c6ae1d20504e7b1ee8f8486d84",
  "x-runtime": "0.01583",
  "x-transaction": "5f8014f32e17f191",
  "x-transaction-mask": "a6183ffa5f8ca943ff1b53b5644ef114df9d6bba"
}
{
  "hourly_limit": 150,
  "remaining_hits": 149,
  "reset_time": "Sun Jun 24 20:31:37 +0000 2012",
  "reset_time_in_seconds": 1340569897
}
authenticated
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "155",
  "content-type": "application/json; charset=utf-8",
  "date": "Sun, 24 Jun 2012 19:33:59 GMT",
  "etag": "\"fed2f4231d1f3af7eb63b975670a14a3\"",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sun, 24 Jun 2012 19:33:59 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "k=10.34.103.114.1340566439857841; path=/; expires=Sun, 01-Jul-12 19:33:59 GMT; domain=.twitter.com, guest_id=v1%3A134056643986291784; domain=.twitter.com; path=/; expires=Wed, 25-Jun-2014 07:33:59 GMT, dnt=; domain=.twitter.com; path=/; expires=Thu, 01-Jan-1970 00:00:00 GMT, lang=en; path=/, twid=u%3D15960972%7CEHcJeY9U4LH8QM%2FkwmMDoB7WmYE%3D; domain=.twitter.com; path=/; secure, _twitter_sess=BAh7CCIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMGH%252FB84AToHaWQiJTc1%250AZDQzNmI1YjljODY3OWFkYWE0MWUzYTU3NTMyOWRl--a5f56214125c5185de126a664098e82ae21dbc2d; domain=.twitter.com; path=/; HttpOnly",
  "status": "200 OK",
  "vary": "Accept-Encoding",
  "x-frame-options": "SAMEORIGIN",
  "x-mid": "966d8ca4a1ed90fee7f58cd9f7a09ac5360c59da",
  "x-runtime": "0.02080",
  "x-transaction": "8eaa9e521c83a433",
  "x-transaction-mask": "a6183ffa5f8ca943ff1b53b5644ef114df9d6bba"
}
{
  "hourly_limit": 0,
  "photos": {
    "daily_limit": 30,
    "remaining_hits": 30,
    "reset_time": "Mon Jun 25 19:33:59 +0000 2012",
    "reset_time_in_seconds": 1340652839
  },
  "remaining_hits": 0,
  "reset_time": "Sun Jun 24 20:33:59 +0000 2012",
  "reset_time_in_seconds": 1340570039
}

Another run
========= Anonymous
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "122",
  "content-type": "application/json; charset=utf-8",
  "date": "Sun, 15 Jul 2012 16:11:52 GMT",
  "etag": "\"e72ed05c9cb68b7d1870d1347811497d\"",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sun, 15 Jul 2012 16:11:52 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "k=10.36.22.126.1342368712289980; path=/; expires=Sun, 22-Jul-12 16:11:52 GMT; domain=.twitter.com, guest_id=v1%3A134236871229314335; domain=.twitter.com; path=/; expires=Wed, 16-Jul-2014 04:11:52 GMT, _twitter_sess=BAh7CCIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCGYGaYs4AToHaWQiJTdj%250AMjcyMjRiYTA3M2JlYTMzMDNhMTE4YTcyMDI0OTFi--c260efcd28b00154e348a4c88ff3c2b86d55b5b4; domain=.twitter.com; path=/; HttpOnly",
  "status": "200 OK",
  "vary": "Accept-Encoding",
  "x-frame-options": "SAMEORIGIN",
  "x-mid": "c993133d070af5992bb365aa40c19e9d5cb3bba7",
  "x-runtime": "0.01314",
  "x-transaction": "16e678deac1d4786",
  "x-transaction-mask": "a6183ffa5f8ca943ff1b53b5644ef114acbe67e5"
}
{
  "hourly_limit": 150,
  "remaining_hits": 150,
  "reset_time": "Sun Jul 15 17:11:52 +0000 2012",
  "reset_time_in_seconds": 1342372312
}
======== With OAuth
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "160",
  "content-type": "application/json; charset=utf-8",
  "date": "Sun, 15 Jul 2012 16:11:52 GMT",
  "etag": "\"a549ecb770b9ca8262d145cd5de0e707\"",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sun, 15 Jul 2012 16:11:52 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "k=10.36.23.102.1342368712578856; path=/; expires=Sun, 22-Jul-12 16:11:52 GMT; domain=.twitter.com, guest_id=v1%3A13423687125825966; domain=.twitter.com; path=/; expires=Wed, 16-Jul-2014 04:11:52 GMT, dnt=; domain=.twitter.com; path=/; expires=Thu, 01-Jan-1970 00:00:00 GMT, lang=en; path=/, twid=u%3D15960972%7CEHcJeY9U4LH8QM%2FkwmMDoB7WmYE%3D; domain=.twitter.com; path=/; secure, _twitter_sess=BAh7CDoPY3JlYXRlZF9hdGwrCJ0HaYs4AToHaWQiJTYwYzZiZmE5NjRlMzk5%250AZGM3NDg1ZGZjYjJkYzIzODdjIgpmbGFzaElDOidBY3Rpb25Db250cm9sbGVy%250AOjpGbGFzaDo6Rmxhc2hIYXNoewAGOgpAdXNlZHsA--de8e71e0eeba9976d38cc705b1e0f8e4e198f70d; domain=.twitter.com; path=/; HttpOnly",
  "status": "200 OK",
  "vary": "Accept-Encoding",
  "x-access-level": "read",
  "x-frame-options": "SAMEORIGIN",
  "x-mid": "0345e7c804f24d079ffe8aba3dc0ce80f40af4d1",
  "x-runtime": "0.03153",
  "x-transaction": "93d21eb2c7c2cf07",
  "x-transaction-mask": "a6183ffa5f8ca943ff1b53b5644ef114acbe67e5"
}
{
  "hourly_limit": 350,
  "photos": {
    "daily_limit": 30,
    "remaining_hits": 30,
    "reset_time": "Mon Jul 16 16:11:52 +0000 2012",
    "reset_time_in_seconds": 1342455112
  },
  "remaining_hits": 350,
  "reset_time": "Sun Jul 15 17:11:52 +0000 2012",
  "reset_time_in_seconds": 1342372312
}

'''
