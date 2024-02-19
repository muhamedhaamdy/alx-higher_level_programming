#!/usr/bin/python3
"""Cities in state"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """City model"""
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'))
