import sqlite3
from sqlite3 import Error
from sqlite3 import dbapi2 as sqlite
import csv

# Database Connection Creation Function:
# This function uses the sqlite3 library to create a sql database connection to the provided db file
# Input: db_file - a .db file that hosts sql tables
# Output: a connection object to the database or Error if connection cannot be established
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# Database Query Function:
#  This function uses the database connection object and creates a cursor object that runs executable commands on the db. A sql query to run is passed to the function, full query result is saved to a variable with each returned row printed to the console to view query results.
# INPUT: conn - connection object to sqlite db
#        query - sql query to run against the db
# OUTPUT: number of rows returned by the query
def db_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    return len(rows)

# Database Info Helper Function:
# This function runs simple select query on provided table to load table metadata. The first item (column name) of the stored metadata is parsed into a column list.
# INPUT: conn - connection object to sqlite db
#        tbl_name - name of the table in db
# OUTPUT: list of column names in the provided table
def db_getinfo(conn, tbl_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + tbl_name)
    column_name_list = [tuple[0] for tuple in cur.description]

    return column_name_list

# CSV Loader Function:
# This function uses the db connection created above, a raw csv file path, and a destination table name to open and read the csv file using python's built in csv library.
# Then the function builds a base SQL statement to INSERT into the using the proper columns names (first row of the csv) and creates a placeholder list for the values section of the SQL statement (?,?, etc) for the len of rows of the csv file
# The function then iterates through the csv rows and uses the same column names to build the list of values
# Lastly, using those formatted rows of values and the INSERT statement string - passes to the executemany function which does a bulk insert to the table
def loadcsv(conn, file_name, tbl_name):
    # PLEASE DESCRIBE -
    csv_file = open(file_name)
    csv_reader = csv.DictReader(csv_file)
    insert_sql = 'INSERT INTO ' + tbl_name + ' (' + ','.join(csv_reader.fieldnames) + ') VALUES (' + ','.join(['?'] * len(csv_reader.fieldnames))+ ')'
    print(insert_sql)
    # PLEASE DESCRIBE -
    values = []
    for datarow in csv_reader:
        row_values = []
        for field in csv_reader.fieldnames:
            row_values.append(datarow[field])
        values.append(row_values)

    conn.executemany(insert_sql, values)
    conn.commit()
