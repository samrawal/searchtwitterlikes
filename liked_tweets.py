# via Twitter API sample code:
# https://github.com/twitterdev/Twitter-API-v2-sample-code/

import requests
import os
import json
import cacheutils as cu

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")


def create_url(user_id="none"):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id"
    # Be sure to replace your-user-id with your own user ID or one of an authenticating user
    # You can find a user ID by using the user lookup endpoint
    id = user_id#"your-user-id"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/users/{}/liked_tweets".format(id)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikedTweetsPython"
    return r


def connect_to_endpoint(url, pagination_token=None):
    parameters = {
        "tweet.fields": "author_id",
        "pagination_token": pagination_token,
    }
    response = requests.request(
        "GET", url, auth=bearer_oauth, params=parameters)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_liked_tweets(uid):
        url = create_url(uid)
        json_response = connect_to_endpoint(url) # {data, meta}
        
        all_tweets = json_response["data"]
        next_token = json_response["meta"].get("next_token", None)

        if cu.is_cached(uid, json_response["data"]):
            return cu.get_cache(uid)
        cu.update_cache(uid, json_response["data"])

        while next_token is not None:
            json_response = connect_to_endpoint(url, next_token) # {data, meta}
            # print(json_response)
            # exit()
            next_token = json_response["meta"].get("next_token", None)
            if "data" not in json_response:
                break
            if cu.is_cached(uid, json_response["data"]):
                return cu.get_cache(uid)
            cu.update_cache(uid, json_response["data"])
            all_tweets += json_response["data"]

            print(f"{len(all_tweets)=}. {json_response['meta']=}")
        return all_tweets
         
        
        #urls = get_tweet_data([x["id"] for x in json_response["data"]])
        #return json_response


if __name__ == "__main__":
    from user_id import get_user_id 
    
    uid = get_user_id("samarthrawal")
    get_liked_tweets(uid)
