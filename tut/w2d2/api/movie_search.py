""" OMDB movie search api """

import requests as re
from flask import request
from secrets import secrets
from __main__ import app

class movie_search_api:
    """ movies search """
    APIKEY = secrets['OMDB']

    def movie_search(self, query, type, year, page):
        """ fetches movies data based on query """
        url = f"http://www.omdbapi.com/?apikey={self.APIKEY}&s={query}"

        if type:
            url = url + f"&type={type}"
        if year:
            url = url + f"&y={year}"
        if page: 
            url = url + f"&page={page}"

        result = re.get(url).json()
        return result

search_api = movie_search_api()

@app.get("/movie")
def search_result():
    """ flask response """
    query = request.args.get('query')
    type = request.args.get('type')
    year = request.args.get('year')
    page = request.args.get('page')

    return search_api.movie_search(query=query, type=type, year=year, page=page)
