from rank_bm25 import BM25Okapi
from user_id import get_user_id
from liked_tweets import get_liked_tweets
from utils import get_tweet_url
from nltk.tokenize import word_tokenize

import nltk

def tweetsearch_bm25(USER_ID, SEARCH_QUERY, TOP_N=100):
    uid = get_user_id(USER_ID)
    liked_tweets = get_liked_tweets(uid)
    
    #liked_tweets = liked_tweets["data"]
    liked_tweet_text = [t["text"] for t in liked_tweets]
    
    tokenized_tweets = [word_tokenize(doc.lower()) for doc in liked_tweet_text]
    tokenized_query = word_tokenize(SEARCH_QUERY.lower())
    bm25 = BM25Okapi(tokenized_tweets)
    scores = bm25.get_scores(tokenized_query)
    #rank_results = bm25.get_top_n(tokenized_query, tokenized_tweets, n=TOP_N)
    
    assert len(liked_tweets) == len(scores)
    res = [{"data": lt, "url": get_tweet_url(lt), "score": sc} for lt, sc in zip(liked_tweets, scores)]
    res.sort(reverse=True, key=lambda x: x["score"])
    total_res = len(res)
    res = list(filter(lambda x: x["score"] > 0, res))
    return res, total_res	
