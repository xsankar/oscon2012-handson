#!/usr/bin/env python
import requests
import json
from requests.auth import HTTPBasicAuth
import datetime
import time
from oauth_hook import OAuthHook

def get_oauth_client():
    """
    Create an application at https://dev.twitter.com/apps
    Copy the credentials here
    """
    consumer_key = "<consumer key>"
    consumer_secret = "<consumer secret>"
    access_token = "<access token>"
    access_token_secret = "<access token secret>"
    header_auth = True
    oauth_hook = OAuthHook(access_token, access_token_secret, consumer_key, consumer_secret, header_auth)
    client = requests.session(hooks={'pre_request': oauth_hook})
    return client

# Get followers
def get_followers(user_id):
    url = 'https://api.twitter.com/1/followers/ids.json'
    payload={"user_id":user_id} # if cursor is needed {"cursor":-1,"user_id":scr_name}
    r = requests.get(url, params=payload)
    print "Get Followers"
    if (r.status_code == 200):
        print json.dumps(r.headers,sort_keys=True,indent=2)
        follower_ids = r.json["ids"]
        return (follower_ids,r.status_code,r.headers["status"])
    else:
        print json.dumps(r.headers,sort_keys=True,indent=2)
        return ([],r.status_code,r.headers["status"])
#    time.sleep(3600)

# Get friends
def get_friends(user_id):
    url = 'https://api.twitter.com/1/friends/ids.json'
    payload={"user_id":user_id} # if cursor is needed {"cursor":-1,"user_id":scr_name}
    r = requests.get(url, params=payload)
    print "Get Friends"
    if (r.status_code == 200):
        print json.dumps(r.headers,sort_keys=True,indent=2)
        friend_ids = r.json["ids"]
        return (friend_ids,r.status_code,r.headers["status"])
    else:
        print json.dumps(r.headers,sort_keys=True,indent=2)
        return ([],r.status_code,r.headers["status"])
#    time.sleep(3600)

# Get followers
def get_followers_with_oauth(user_id,client):
    url = 'https://api.twitter.com/1/followers/ids.json'
    payload={"user_id":user_id} # if cursor is needed {"cursor":-1,"user_id":scr_name}
    r = client.get(url, params=payload)
    print "Get Followers"
    if (r.status_code == 200):
        print json.dumps(r.headers,sort_keys=True,indent=2)
        follower_ids = r.json["ids"]
        return (follower_ids,r.status_code,r.headers["status"])
    else:
        print json.dumps(r.headers,sort_keys=True,indent=2)
        return ([],r.status_code,r.headers["status"])
#    time.sleep(3600)

# Get friends
def get_friends_with_oauth(user_id,client):
    url = 'https://api.twitter.com/1/friends/ids.json'
    payload={"user_id":user_id} # if cursor is needed {"cursor":-1,"user_id":scr_name}
    r = client.get(url, params=payload)
    print "Get Friends"
    if (r.status_code == 200):
        print json.dumps(r.headers,sort_keys=True,indent=2)
        friend_ids = r.json["ids"]
        return (friend_ids,r.status_code,r.headers["status"])
    else:
        print json.dumps(r.headers,sort_keys=True,indent=2)
        return ([],r.status_code,r.headers["status"])
#    time.sleep(3600)
