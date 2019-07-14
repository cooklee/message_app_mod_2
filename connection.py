from psycopg2 import connect

from settings import dbinfo


def get_connection(settings=None, autocommit=True):
    if settings is None:
        settings = dbinfo
    cnx = connect(**settings)
    cnx.autocommit = autocommit
    return cnx

if __name__ == "__main__":
    connection = get_connection()
    connection.close()
