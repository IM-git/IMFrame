import sqlite3
import os
from src import SQLRequests


class ToolsDatabase:

    @staticmethod
    def open_db():
        """Will open database or if database not exists,
        create database - name_database.db"""
        connection = sqlite3.connect(SQLRequests.NAME_DATABASE)
        db_session = connection.cursor()
        return db_session

    @staticmethod
    def close_db(db_session):
        """Will closed database session."""
        db_session.connection.commit()
        db_session.close()

    @staticmethod
    def create_db():
        """Will create table in database
        with the specified parameters."""
        db_session = ToolsDatabase.open_db()
        db_session.execute(SQLRequests.CREATE_TABLE)
        ToolsDatabase.close_db(db_session)

    @staticmethod
    def insert_into_db():
        """Will insert values into the table."""
        db_session = ToolsDatabase.open_db()
        db_session.executemany(SQLRequests.INSERT_INTO_TABLE, SQLRequests.VALUES)
        ToolsDatabase.close_db(db_session)

    @staticmethod
    def read_db():
        """Getting value/values from the 'users' table."""
        db_session = ToolsDatabase.open_db()
        values = db_session.execute(SQLRequests.SELECT_TABLE)
        #   Prints all values to the console
        print(values.fetchall())
        ToolsDatabase.close_db(db_session)

    @staticmethod
    def delete_table():
        """Delete table in name_database.db database,
        but the database will remain(empty)."""
        db_session = ToolsDatabase.open_db()
        db_session.execute(SQLRequests.DELETE_TABLE)
        ToolsDatabase.close_db(db_session)

    @staticmethod
    def delete_db():
        """The name_database.db database will be deleted."""
        os.remove(SQLRequests.NAME_DATABASE)
