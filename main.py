import flask
from flask import Flask, request, current_app, render_template
from engine import tweetsearch


app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/search")
def search():
    error_str = '''
       <h1>Looks like my Twitter API has been temporarily rate-limited. You can try again in ~15 mins or: </h1>
       <p style="font-family: monospace">
        <a href="https://replit.com/@samrawal/searchtwitterlikes">clone this Repl</a> and enter your own Twitter API keys into the Secrets section. (TWITTER_BEARER_TOKEN)
        </p>
    '''
    username = request.args.get("username")
    query = request.args.get("query")
    # res, total = tweetsearch(username, query)

    try:
        res, total = tweetsearch(username, query)
    except:
        return error_str
        
    searchresults = "<hr>"
    for i, r in enumerate(res):
        searchresults += "{4}{0}. {1} ({2}). BM25 score={3:.5f}</p> <hr>".format(
                i+1,
                r["data"]["text"],
                "<a href={0}>{0}</a>".format(r["url"]),
                r["score"],
                "<p style=\"color:grey\">" if r["score"] == 0 else "<p>"
        )
    
    html = '<html><meta name="viewport" content="width=device-width, initial-scale=1.0"><body>{}</body></html>'
    res_html = "<h1> Searching {}'s {} likes for query \"{}\":</h1><br>".format(username, total, query) + searchresults
    return html.format(res_html)

	
if __name__ == "__main__":
    app.run(
		host='0.0.0.0',
		port='9999',
		)