#!/usr/bin/python3
"""A flask application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns the string hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns the string HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns the string c + whatever text is after"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Returns the string python + whatver text comes after it"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
def python():
    """Returns the string python is cool"""
    return "Python is cool"


@app.route('/number/int:<n>', strict_slashes=False)
def number(n):
    """returns a statement that prints the value of n if int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
