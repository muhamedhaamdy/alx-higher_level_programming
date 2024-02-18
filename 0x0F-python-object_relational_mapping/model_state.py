#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
