import argparse
from engine import tweetsearch_bm25

def search(username, query):
    error_str = '''
        <h1>Looks like my Twitter API has been temporarily rate-limited. You can try again in ~15 mins or: </h1>
        <p style="font-family: monospace">
        <a href="https://replit.com/@samrawal/searchtwitterlikes">clone this Repl</a> and enter your own Twitter API keys into the Secrets section. (TWITTER_BEARER_TOKEN)
        </p>
    '''

    try:
        res, total = tweetsearch_bm25(username, query)
    except:
        return error_str


    for i, r in enumerate(res):
        print("{4}{0}. {1} ({2}). BM25 score={3:.5f}".format(
                i+1,
                r["data"]["text"],
                r["url"],
                r["score"],
                ""
        ))
        print("\n" + "="*100 + "\n")
    
	
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python App with Username and Query Arguments')
    parser.add_argument('-u', '--username', type=str, help='Username')
    parser.add_argument('-q', '--query', type=str, help='Query')
    parser.add_argument('-r', '--ranking', type=str, choices=['bm25', 'embeddings'], default='bm25',
                        help='Ranking method')

    args = parser.parse_args()
    search(args.username, args.query)
