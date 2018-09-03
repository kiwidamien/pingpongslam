from flask import Flask, abort, render_template, jsonify, request
from .pingpong_api import *
from .make_app import app
from .leaderboard import pull_leaderboard

def you_can_challenge(username):
    #Record player's name
    player = username

    if is_player_valid(player) == False:
        response = f"{player} doesn't exist. Please enter a valid player's username."
        return jsonify(response)
    else:
        leaderboard = pull_leaderboard()
        candidate_list = get_two_players_above(player, leaderboard)
        response = candidate_list

    return response

@app.route('/api/<username>/can_challenge', methods=['GET'])
def you_can_challenge_api(username):
    #Record player's name
    return jsonify(you_can_challenge(username))
