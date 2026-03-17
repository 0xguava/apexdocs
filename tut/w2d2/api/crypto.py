""" crypto currency rate tracker """

import requests as re
from flask import request
from secrets import secrets
from __main__ import app

class crypto_price_api:
    APIKEY = secrets['COINGECKO']

    def get_price(self, crypto, cur):
        url = f"https://api.coingecko.com/api/v3/coins/markets?ids={crypto}&vs_currency={cur}"
        
        result_temp = re.get(url).json()[0]
        result = {}
        for r in ['current_price', 'id']:
            result.update({ r : result_temp[r]})
        result.update({ 'real_curreny' : cur})
        return result

crypto_api = crypto_price_api()

@app.get("/crypto")
def crypto():
    crypto = request.args.get('crypto')
    cur = request.args.get('cur')

    return crypto_api.get_price(crypto=crypto, cur=cur)
