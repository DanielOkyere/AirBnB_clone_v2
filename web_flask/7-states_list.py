#!/usr/bin/python3
"""
Starts a web application on port 5000 for 0.0.0.0
imports storage module
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Lists all the states from db
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_db(exeption):
    """ Closes session for db"""
    storage.close()
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")