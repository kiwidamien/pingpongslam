from flask import Flask
import psycopg2
import urllib.parse as urlparse
import os


app = Flask('test app')

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

@app.route('/')
def index():
    con = psycopg2.connect(
        dname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = con.cursor()
    con.close()
    return "Hello from Flask"

if __name__ == '__main__':
    app.run()
