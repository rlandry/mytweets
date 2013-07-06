# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from django.http import HttpResponse
import json

# Settings -- you could move these to your settings.py and import them
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"

OAUTH_TOKEN = "YOUR_OAUTH_TOKEN"
OAUTH_TOKEN_SECRET = "YOUR_OATH_SECRET"

SCREEN_NAME = 'YOUR_SCREENNAME'
TWEET_COUNT = '1'  # Number of tweets you'd like to retrieve

def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]
    
    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url
    
    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        r = requests.get(url="https://api.twitter.com/1.1/statuses/mentions_timeline.json", auth=oauth)
        print r.json()


# ------------------------------------------------------------------------------------------

def get_recent_tweets(request):
    lResume = []
    oauth = get_oauth()
    url_string = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + SCREEN_NAME + "&count=" + TWEET_COUNT
    r = requests.get(url=url_string, auth=oauth)
    lTweets = r.json()
    for dTweet in lTweets:
        lResume.append(dTweet['text'])
    return HttpResponse(json.dumps(lResume),mimetype="application/json")
