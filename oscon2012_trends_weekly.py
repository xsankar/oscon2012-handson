#!/usr/bin/env python
import requests
import json
import datetime
import time
import oscon2012_mongo

#
# Trends for a week
#
connection = oscon2012_mongo.connect_to_db()
dbh = oscon2012_mongo.get_db(connection)
assert dbh.connection == connection
print "Got Database handle to %s" % dbh.database
#
url = 'http://api.twitter.com/1/trends/weekly.json'
datelst=["2012-06-23","2012-06-24","2012-06-25","2012-06-26","2012-06-27","2012-06-28","2012-06-29",
         "2012-06-30","2012-07-01","2012-07-02","2012-07-03","2012-07-04","2012-07-05","2012-07-06",
         "2012-07-07","2012-07-08","2012-07-09","2012-07-10","2012-07-11","2012-07-12","2012-07-13",
         "2012-07-14","2012-07-15"]
for val in datelst:
    payload={"date":val}
    r = requests.get(url, params=payload)
    hdrs = json.dumps(r.headers,sort_keys=True,indent=2)
    bdy = json.dumps(r.json,sort_keys=True,indent=2)
    print hdrs
    print bdy
    #
    # Add a record
    # date,header,body
    #
    user_doc = {"date":payload["date"],
                "header":r.headers,
                "body":r.json
                }
    dbh.trendsw.insert(user_doc,safe=True)
