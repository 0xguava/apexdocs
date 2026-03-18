""" ip address information fetch api """

import requests as re
from flask import request
from secrets import secrets
from __main__ import app

class geo_lookup_api:
    """ ip info lookup """
    def get_location(self, ip):
        """ fetches location and other info """
        if ip:
            url = f"http://ip-api.com/json/{ip}"
        else:
            url = f"http://ip-api.com/json/"
        
        re_temp = re.get(url).json()
        result = {}

        for t in ['query', 'country', 'region', 'city', 'zip', 'lat', 'lon', 'isp']:
            result.update({ t : re_temp[t]})

        return result

geo_api = geo_lookup_api()

@app.get("/ip")
def get_ip():
    """ flask response """
    ip = request.args.get('ip')

    return geo_api.get_location(ip=ip)
