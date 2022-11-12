#!/usr/bin/python3
"""
Setting up Airbnb to be live
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the main hbnb filter page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def close_db(exception):
    """ Closes session for db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
