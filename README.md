mytweets
========

Simple Python script to access the Twitter API (v1.1) to collect a list of recent Tweets from a timeline.  Great addition for Django projects.  Uses simple jQuery ajax call for display. 


Dependencies
-------------
Python: requests, requests-oauthlib

Javascript: jQuery

Installation
---------------

1 - Place **mytweets.py** somewhere in your codebase

2 - Register your application with Twitter here: https://dev.twitter.com/apps/new

3 - Enter the values for CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, SCREEN_NAME and TWEET_COUNT (You could move these values to your settings.py and import them)

4 - Add a URL for the json file that gets generated, in your urls.py:  **(r'^get_recent_tweets', 'mytweets.get_recent_tweets'),**

5 - Add a jQuery ajax call ( **get_tweets.js** ) to fetch the data.


