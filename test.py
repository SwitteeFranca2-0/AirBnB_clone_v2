#!/usr/bin/python3
"""See the output of a particular code"""

from models.city import City
from models.state import State
from models import storage

states = storage.all(State).values()
i = 0
j = 0
for state in states:
    j+=1
    print(f'{j, state.name, state.id}')
    for city in state.cities:
        i+= 1
        print(f'{i, city.name, city.id}\n')
