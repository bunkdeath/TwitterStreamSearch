#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Mar 11, 2012 8:29:21 AM$"

import urllib
import pycurl
import json


STREAM_URL = "https://stream.twitter.com/1/statuses/filter.json"

# parameters
pf = {}
USER = "bunkdeath"
PASS = "*********"

def on_receive(data):
    parseStreamingTweet(data)

def parseStreamingTweet(tweet):
    print "\n"
    try:
        singleTweetJson = json.loads(tweet)
        for index in singleTweetJson:
            if index == 'text':
                print "text : ", repr(singleTweetJson[index])
            if index == 'created_at':
                print "created at : ", singleTweetJson[index]
            if index == 'geo':
                print "geo : ", singleTweetJson[index]
            if index == 'in_reply_to_status_id':
                print "in reply to : ", singleTweetJson[index]
            if index == 'user':
                user = singleTweetJson[index]['profile_image_url']
                print "profile pic : ", user
    except ValueError:
        print "Error : ", tweet
        return

def search(track):
    pf['track'] = track
    c = pycurl.Curl()
    c.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
    c.setopt(c.URL, 'https://stream.twitter.com/1/statuses/filter.json')
    c.setopt(c.POSTFIELDS, urllib.urlencode(pf))
    c.setopt(c.VERBOSE, 1)
    c.setopt(pycurl.WRITEFUNCTION, on_receive)
    c.perform()
    c.close()

search('cricket')