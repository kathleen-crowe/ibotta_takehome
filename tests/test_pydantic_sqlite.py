from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

from utils.pydantic_sqlite import (
    normalize_type,
    create_table_sql,
    model_to_row,
    create_insert_sql,
)

class FakeEnum(str, Enum):
    A = "A"


class FakeModel:
    def model_dump(self):
        return {
            "id": 1,
            "name": "test",
            "value": 2.5,
            "type": FakeEnum.A,
            "created_at": datetime(2021, 1, 1, 12, 0, 0),
        }


class PydanticModel(BaseModel):
    id: int
    name: str

def test_normalize_type():
    assert normalize_type(Optional[datetime]) is datetime


def test_model_to_row():
    row = model_to_row(FakeModel())

    assert row[0] == 1
    assert row[1] == "test"
    assert row[3] == "A"
    assert isinstance(row[-1], str)


def test_create_insert_sql():
    assert create_insert_sql("users", ["id", "name"]) == (
        "INSERT INTO users (id, name) VALUES (?, ?)"
    )


def test_create_table_sql():
    sql = create_table_sql(PydanticModel, "users")

    assert "CREATE TABLE IF NOT EXISTS users" in sql
    assert "id INTEGER PRIMARY KEY" in sql
    assert "name TEXT" in sql