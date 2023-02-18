#!/usr/bin/python3
"""Thiis returns the lists of states"""

from flask import Flask
from flask import render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """This closes the session after each request"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Renders a template of the lists of states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states = states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)