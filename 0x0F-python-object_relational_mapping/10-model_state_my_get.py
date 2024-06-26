#!/usr/bin/python3
'''script that lists all State object'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine_path = 'mysql://{}:{}@localhost:3306/{}'\
                .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(engine_path)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like(sys.argv[4]))\
                                .order_by(State.id).all()
    if state:
        print(state[0].id)
    else:
        print('Not found')
