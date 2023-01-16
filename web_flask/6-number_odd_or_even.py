#!/usr/bin/python3
"""A flask application"""

from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """renders a template that contains the value of n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Returns a template regarding whether the value is even or odd"""
    if int(n) % 2:
        return render_template('6-number_odd_or_even.html', n=n, what="odd")
    else:
        return render_template('6-number_odd_or_even.html', n=n, what="even")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)