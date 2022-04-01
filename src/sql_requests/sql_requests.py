import os


class SQLRequests:
    NAME_DATABASE = ""
    CREATE_TABLE = """"""
    INSERT_INTO_TABLE = """"""
    VALUES = ""
    SELECT_TABLE = """"""
    DELETE_TABLE = """"""


class SQLRequestsExample:

    #   The name database file.
    EXAMPLE_NAME_DATABASE = "login_password.db"

    #   This list was created as an example, for using it in EXAMPLE_INSERT_INTO_TABLE
    LIST = [('standard_user', 'secret_sauce'),
            ('locked_out_user', 'secret_sauce'),
            ('problem_user', 'secret_sauce'),
            ('performance_glitch_user', 'secret_sauce')]

    #   The table with three values will be created.
    EXAMPLE_CREATE_TABLE = """CREATE TABLE users(
                            _id INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT,
                            password TEXT)"""

    #   Here is existing one important moment: was created 3 row
    #   but created for inserting in (LIST) two values.
    #   For creating a first value need enter a 'NULL',
    #   see the example below.
    #   Therefore, the first value automatically create a _id, the next two add from a LIST
    EXAMPLE_INSERT_INTO_TABLE = """INSERT INTO users VALUES (NULL, ?, ?)""", LIST

    #   Getting all values from the 'users' table.
    EXAMPLE_READ_TABLE = """SELECT * FROM users"""

    #   Delete table, if table is exist, in the login_password.db database, but the database will remain(empty).
    EXAMPLE_DELETE_TABLE = """DROP TABLE if exists users"""

    #   Delete login_password.db database.
    # EXAMPLE_DELETE_DATA = f"{os.remove('name_database.db')}"
