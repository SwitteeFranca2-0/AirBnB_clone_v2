#!/usr/bin/python3
"""Thiis returns the lists of states"""

from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db():
    """This closes the session after each request"""
    storage.close()

@app.route('/states_list')
def states_list():
    """Renders a template of the lists of states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states_list = states)