import pytest
import sqlite3
from sqlite3 import Error
from src import SQLRequests


@pytest.fixture(scope='session')
def database():
    try:
        connection = sqlite3.connect(SQLRequests.NAME_DATABASE)
        db_session = connection.cursor()
        yield db_session
        db_session.connection.commit()
        db_session.close()
    except Error:
        print(f'Something wrong with sqlite3: {Error}', Error)
