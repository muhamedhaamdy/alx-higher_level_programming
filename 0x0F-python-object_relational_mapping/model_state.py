#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """state model"""
    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column('name', String(128), nullable=False)
