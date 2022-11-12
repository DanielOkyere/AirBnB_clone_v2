#!/usr/bin/python3
"""
States and state
Runs on Port:5000 for host 0.0.0.0
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """ Lists all states if id is not provided"""
    states = storage.all(State)
    if id is None:
        return render_template('9-states.html', state = states)
    else:
        for state in storage.all(State).values():
            if state.id == id:
                return render_template("9-states.html", state = state)
        return render_template('9-states.html')


@app.teardown_appcontext
def close_db(exception):
    """ Closes session for db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")