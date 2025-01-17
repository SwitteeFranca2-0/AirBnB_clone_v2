from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(error):
    """"close the database session incase of an erro"""
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    """List all cities of a state"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
