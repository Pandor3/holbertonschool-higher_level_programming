#!/usr/bin/python3
"""
This module will list all State objects that contains
the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_filtered = session.query(State).filter(State.name.contains('a'))

    for state in states_filtered.order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
