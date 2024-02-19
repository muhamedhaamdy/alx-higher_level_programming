#!/usr/bin/python3
'''prints all City objects from the database'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine_path = 'mysql://{}:{}@localhost:3306/{}'\
                .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(engine_path)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(State.id == City.state_id)\
                    .order_by(City.id).all()
    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
