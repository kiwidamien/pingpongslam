from flask import Flask, abort, render_template, jsonify, request
import psycopg2
from .pingpong_api import *
from .make_app import app

def get_user_history(username):
    player = username
    response = get_history(player)

    return response

@app.route('/api/<username>', methods=['GET'])
def get_user_history_api(username):
    return jsonify(get_user_history(username))
