
import requests as re
from flask import request
from secrets import secrets
from __main__ import app
import time

class quote_api:
    def __init__(self):
        self.cache = {}
        self.last_fetch = 0

    def get_quote(self):
        current_time = time.time()
        if not self.cache or (current_time - self.last_fetch > 3600):
            url = f"https://zenquotes.io/api/today"
            temp = re.get(url).json()[0]
            self.cache.update({'quote of the day' : temp['q']})
            self.cache.update({'author' : temp['a']})
            self.last_fetch = current_time
        
        return self.cache

qotd_api = quote_api()

@app.get("/quote")
def quote():
    return qotd_api.get_quote()
