#!/usr/bin/python3
"""
Script starts a Flask Web Application
Runs on `Port: 5000, host: 0.0.0.0`
Implements strict_slashes=False
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    / Returns "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    /hbnb Returns HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
