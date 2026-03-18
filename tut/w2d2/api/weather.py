""" weather fetch and location cords fetch api """

import requests as re
from flask import request, jsonify
from secrets import secrets
from __main__ import app

class weather_api:
    """ weather api """
    APIKEY = secrets['WEATHER']

    def get_cords(self, city) -> dict:
        """ fetches cordinates of given city """
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={self.APIKEY}"
        location_data = re.get(url)
        cords = {'lat' : location_data.json()[0]["lat"],
                 'lon' : location_data.json()[0]["lon"]}
        return cords

    def get_weather(self, city):
        """ using cordinates fetches weather data  """
        cords = self.get_cords(city)
        lat = cords['lat']
        lon = cords['lon'] 
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.APIKEY}"
        weather_info = re.get(url).json() 
        cache = {key: weather_info[key] for key in ['name', 'main', 'weather']}
        """ cache.update({'timestamp' : time.time()}) """
        return jsonify(cache)

forecast = weather_api()

@app.get("/weather")
def weather():
    """ flask response """
    city = request.args.get('city')
    if not city:
        return "Please provide query for city name", 400
    return forecast.get_weather(city) 
