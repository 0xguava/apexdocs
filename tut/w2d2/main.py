""" Assignment of w2d2: APIs """

from flask import Flask

app = Flask(__name__)

import api.weather
import api.github
import api.movie_search
import api.news
import api.currency
import api.holiday
import api.crypto
import api.quote
import api.ip

if __name__ == "__main__":
    app.run()
