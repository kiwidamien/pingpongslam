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
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = con.cursor()
    cursor.execute('SELECT * FROM player;')
    results = cursor.fetchall()
    con.close()
    return f"Hello from Flask, {str(results)}"

if __name__ == '__main__':
    app.run()
