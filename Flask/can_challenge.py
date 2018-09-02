from flask import Flask, abort, render_template, jsonify, request
import datetime as dt
import psycopg2
from pingpong_api import *
from make_app import app

@app.route('/api/<username>/can_challenge', methods=['GET'])
def can_challenge(username):
    #Connect to the database and create a cursor
    player = username

    #WILL HAVE TO BE REPLACED BY JENMEENT'S FUNCTION FOR LEADERBOARD
    leaderboard = [{'id':'jwong','record':'52-0','previous_rank':'1'},
                       {'id':'brett','record':'26-7','previous_rank':'2'},
                       {'id':'damien','record':'24-3','previous_rank':'3'}]

    candidate_list = get_two_players_above(player, leaderboard)

    response = candidate_list

    conn.close()

    return jsonify(response)
