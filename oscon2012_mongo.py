#!/usr/bin/env python
import pymongo
import datetime
import time

"""
Install mongo, pymong and start a mongo server
Fillin server_name, password, admin user, admin user password
"""
print "pymongo version = ",pymongo.version

def connect_to_db():
    server_url=""
    server_port=27017
    connection = pymongo.Connection(server_url,server_port)
    print 'Connected to DB!'
    return connection

def get_db(connection):
    admin_user=""
    admin_password=""
    dbh = connection["admin"]
    dbh.authenticate(admin_user,admin_password)
    dbh = connection["analytics"] # admin"]
    return dbh

def find_a_record(dbh,colxn_name,query):
    colxn = dbh[colxn_name]
    #print colxn
    #print colxn.find().count()
    cursor = colxn.find(query) #find()
    return cursor

def find_all_records(dbh,colxn_name):
    colxn = dbh[colxn_name]
    #print colxn
    #print colxn.find().count()
    cursor = colxn.find() #find()
    return cursor

def update_a_record(dbh,colxn_name,u1,u2):
    colxn = dbh[colxn_name]
    colxn.update(u1,u2,safe=True)
