#!/usr/bin/python3
"""
States and state
Runs on Port:5000 for host 0.0.0.0
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """ Lists all states if id is not provided"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)



@app.teardown_appcontext
def close_db(exception):
    """ Closes session for db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
