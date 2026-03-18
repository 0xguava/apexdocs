""" news headline fetch api """

import requests as re
from flask import request, jsonify
from secrets import secrets
from __main__ import app

class news_api:
    """ news api class """
    APIKEY = secrets['NEWSAPI']

    def fetch_headlines(self, query, con, no):
        """ fetches headlines with or without query """
        url = f"https://newsapi.org/v2/top-headlines?apiKey={self.APIKEY}"

        if query:
            url = url + f"&q={query}"
        if con:
            url = url + f"&country={con}"
        if no:
            url = url + f"&pageSize={no}"

        news = re.get(url).json()['articles']
        headlines = []
        for n in news:
            headlines.append(n['title'])
        return jsonify(headlines)

news = news_api()

@app.get('/news')
def headlines():
    """ flask response """
    query = request.args.get('query')
    con = request.args.get('con')
    no = request.args.get('no')

    return news.fetch_headlines(query=query, con=con, no=no)
    
