""" holiday chart api """

import requests as re
from flask import request
from secrets import secrets
from __main__ import app

class holiday_api:
    """ holiday api """

    def get_holidays(self, year, con):
        """ fetches holiday list for give country """
        url = f"https://date.nager.at/api/v3/publicholidays/{year}/{con}"
        
        result = re.get(url).json()
        return result

holiday_service = holiday_api()

@app.get("/holidays")
def holidays():
    """ flask response """
    year = request.args.get('year')
    con = request.args.get('con')

    return holiday_service.get_holidays(year=year, con=con)
