#!/usr/bin/python3
"""
Script starts a Flask Web Application
Runs on `Port: 5000, host: 0.0.0.0`
Implements strict_slashes=False
"""

from flask import Flask, escape, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    /c/<text> Returns C followed byt the value of text
    """
    text = text.replace("_", " ")
    return "C %s" % escape(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text=None):
    """
    /Python/(<text>)
    """
    if text is None:
        return "Python is cool"
    else:
        return "Python %s" % escape(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    /number/<n> Route only returns number
    """
    if isinstance(n, int):
        return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    /number_template/<n> Returns page only if n is a integer
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Number Checks if number is even or odd"""
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
