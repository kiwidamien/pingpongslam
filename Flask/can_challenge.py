from flask import Flask, abort, render_template, jsonify, request
import datetime as dt
import psycopg2
from pingpong_api import *
from make_app import app

@app.route('/api/<username>/can_challenge', methods=['GET'])
def you_can_challenge(username):
    #Record player's name
    player = username

    if is_player_valid(player) == False:
        response = f"{player} doesn't exist. Please enter a valid player's username."
        return jsonify(response)

    else:
        #WILL HAVE TO BE REPLACED BY JENMEENT'S FUNCTION FOR LEADERBOARD
        leaderboard = [{'id':'Jenn Ifer','record':'52-0','previous_rank':'1'},
                           {'id':'Brett','record':'26-7','previous_rank':'2'},
                           {'id':'Damien','record':'24-3','previous_rank':'3'}]

        candidate_list = get_two_players_above(player, leaderboard)
        response = candidate_list

    return jsonify(response)
