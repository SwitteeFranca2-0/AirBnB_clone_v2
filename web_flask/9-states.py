from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """"close the database session incase of an erro"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """display a html page"""
    rn = 1
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, run=rn)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Show a state with a given id"""
    states = storage.all(State).values()
    dic = {state.id: state for state in states}
    if id in dic.keys():
        h3 = 'Cities'
        h1 = 'State'
        return render_template('9-states.html', states=dic[id].cities,
                               show_h3=h3, tag=h1, name=dic[id].name)
    else:
        no_content = 1
        return render_template('9-states.html', no_content=no_content)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
