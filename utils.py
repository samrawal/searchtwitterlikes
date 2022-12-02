def get_tweet_url(payload:dict):
	return "https://twitter.com/{}/status/{}".format(
		payload["author_id"],
		payload["id"]
	)