import os
import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    if (os.environ.get('DOCKER_CONTAINER', False)): 
        pgsqlhost = 'dbpg'
    else: 
        pgsqlhost = config('PGSQL_HOST')

    try:
        return psycopg2.connect(
            host = pgsqlhost,
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex