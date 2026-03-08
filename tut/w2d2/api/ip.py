
import requests as re
from flask import request
from secrets import secrets
from __main__ import app

class geo_lookup_api:
    def get_location(self, ip):
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
    ip = request.args.get('ip')

    return geo_api.get_location(ip=ip)
