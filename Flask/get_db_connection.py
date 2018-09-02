import psycopg2 as pg
import urllib.parse as urlparse
import os

def get_connection():
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    dbname = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port

    con = pg.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    return con
