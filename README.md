mytweets
========

Simple Python script to access the Twitter API (v1.1) to collect a list of recent Tweets from a timeline.  Great addition for Django projects.  Uses a simple jQuery ajax call for display. 

Based on blog posts by [Thomas Sileo](http://thomassileo.com/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/) and [aviras](http://aviras.wordpress.com/2013/06/17/get-recent-tweets-from-1-1-api-django-jquery/).


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


