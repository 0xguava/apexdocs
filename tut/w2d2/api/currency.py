""" currency conversion api """

import requests as re
from flask import request, jsonify
from secrets import secrets
from __main__ import app

class currency_conversion_api:
    """ currency conversion api """
    APIKEY = secrets['CURRENCY']

    def get_conversion(self, base_code, target_code, amt):
        """ currency rate fetch and conversion function """
        url = f"https://v6.exchangerate-api.com/v6/{self.APIKEY}/pair/{base_code}/{target_code}"
        
        if amt:
            url = url + f"/{amt}"

        result_temp = re.get(url).json()
        result = {}

        for t in ['base_code', 'target_code', 'conversion_rate']:
            result.update({t : result_temp[t]})

        if amt:
            result.update({'conversion_result' : result_temp['conversion_result']})

        return jsonify(result)

conversion_api = currency_conversion_api()

@app.get('/currency')
def currency_ex():
    """ flask response """
    base_code = request.args.get('base')
    target_code = request.args.get('to')
    amt = request.args.get('amt')

    return conversion_api.get_conversion(base_code=base_code, target_code=target_code, amt=amt)
