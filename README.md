# search twitter likes

Quick barebones app to search your or any public Twitter user's likes.

Currently running on searchtwitterlikes.samrawal.repl.co/ (may take little bit of time to start up.)

Uses my Twitter API key which could get rate-limited, so most straightforward thing to do would be to clone this repo or fork project on Replit and add your own API key. (Set your bearer token to env variable `TWITTER_BEARER_TOKEN`)


### Under the hood:
- Uses code adapted from [Twitter v2 API](https://github.com/twitterdev/Twitter-API-v2-sample-code/).
- Uses the [rank-bm25](https://pypi.org/project/rank-bm25/) Python package to rank searching.