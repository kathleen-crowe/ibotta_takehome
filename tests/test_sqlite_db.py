import pytest
from pydantic import BaseModel

from utils.sqlite_db import SQLiteDB


# -----------------------
# Fake model
# -----------------------

class User(BaseModel):
    id: int
    name: str


# -----------------------
# Tests
# -----------------------

def test_create_table_and_insert():
    db = SQLiteDB(":memory:")

    # create table
    db.create_table(User, "users")

    # insert data
    users = [
        User(id=1, name="Alice"),
        User(id=2, name="Bob"),
    ]

    db.insert_data(User, "users", users)

    # verify data was inserted
    rows = db.execute("SELECT * FROM users ORDER BY id")

    assert rows == [
        (1, "Alice"),
        (2, "Bob"),
    ]

    db.close()


def test_insert_data_handles_duplicates_gracefully():
    db = SQLiteDB(":memory:")

    db.create_table(User, "users")

    user = User(id=1, name="Alice")

    db.insert_data(User, "users", [user])

    # inserting same PK again should trigger your error handling path
    with pytest.raises(Exception):
        db.insert_data(User, "users", [user])

    db.close()