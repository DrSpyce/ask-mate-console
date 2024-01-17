import psycopg2
from psycopg2 import extras
import os


def connect_to_db():
    db_uri = os.environ['db_connection']
    try:
        connection = psycopg2.connect(db_uri)
    except psycopg2.DatabaseError as exception:
        print("Db connection could not be established")
        raise exception
    connection.autocommit = True
    return connection


def execute_query(query_string, query_parameters=None):
    with connect_to_db() as connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query_string, query_parameters)
            result = cursor.fetchall()
    return result
