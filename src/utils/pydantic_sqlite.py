from datetime import datetime
from typing import get_origin, Union
from enum import Enum

SQL_TYPE_MAP = {
    int: "INTEGER",
    str: "TEXT",
    float: "REAL",
    datetime: "TIMESTAMP",
    bool: "INTEGER"
}

def normalize_type(annotation):
    origin = get_origin(annotation)

    if origin is Union:
        args = [a for a in annotation.__args__ if a is not type(None)]
        return args[0] if args else annotation

    return annotation

def create_table_sql(model, table_name: str):
    fields = model.model_fields

    columns = []

    for name, field in fields.items():
        py_type = normalize_type(field.annotation)
        sql_type = SQL_TYPE_MAP.get(py_type, "TEXT")

        col_def = f"{name} {sql_type}"

        if name == "id":
            col_def += " PRIMARY KEY"

        columns.append(col_def)

    return f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(columns)}
    );
    """

def model_to_row(instance):
    """
    Convert a Pydantic model instance into a DB-ready tuple.
    """
    values = []

    for v in instance.model_dump().values():
        if isinstance(v, Enum):
            values.append(v.value)
        elif isinstance(v, datetime):
            values.append(v.isoformat())
        else:
            values.append(v)

    return tuple(values)

def create_insert_sql(table_name: str, columns: list):
    col_names = ", ".join(columns)
    placeholders = ", ".join(["?"] * len(columns))
    return f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"