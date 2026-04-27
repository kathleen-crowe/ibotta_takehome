import sqlite3
from utils.pydantic_sqlite import create_table_sql
from utils.pydantic_sqlite import create_insert_sql
from utils.pydantic_sqlite import model_to_row


class SQLiteDB:
    """
    Lightweight wrapper around SQLite connection and cursor.
    Ensures single connection per instance and reusable DB operations.
    """

    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        """Create connection and cursor if not already created."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
    
    def create_table(self, model, table_name: str):
        """
        Create a table based on a Pydantic model schema.
        """
        query = create_table_sql(model, table_name)
        self.execute(query)

    def insert_data(self, model, table_name: str, records: list):
        """
        Insert data into a table using a list of Pydantic model instances.
        Converts models to tuples and uses executemany for efficiency.
        """
        columns = list(model.model_fields.keys())
        query = create_insert_sql(table_name, columns)
        values = [model_to_row(record) for record in records]

        try:
            print(f"Inserting {len(values)} records into {table_name}...")
            self.executemany(query, values)
            print(f"Successfully inserted into {table_name}")
        except sqlite3.IntegrityError as e:
            print(f"\n❌ Data integrity error while inserting into '{table_name}'")
            print(f"Reason: {e}")
            raise

    def execute(self, query: str):
        """Execute a SQL query and return fetched rows."""
        self.connect()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def executemany(self, query: str, values: list):
        """Bulk insert/update."""
        self.connect()
        self.cursor.executemany(query, values)
        self.conn.commit()

    def get_columns(self, table_name: str):
        """Return column names using cursor metadata."""
        self.connect()
        self.cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")
        return [col[0] for col in self.cursor.description]

    def close(self):
        """Close connection safely."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None