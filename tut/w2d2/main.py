""" Assignment of w2d2: APIs """

from flask import Flask

app = Flask(__name__)

import api.weather
import api.github

if __name__ == "__main__":
    app.run()
