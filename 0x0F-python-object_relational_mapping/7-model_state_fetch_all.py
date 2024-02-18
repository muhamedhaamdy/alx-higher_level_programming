#!/usr/bin/python3
'''script that lists all State object'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


engine_path = 'mysql://{}:{}@localhost:3306/{}'\
                .format(sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(engine_path)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).all()
states
