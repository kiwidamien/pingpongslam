from flask import Flask, abort, render_template, jsonify, request
from pingpong_api import *

app = Flask('PingPongApp')

@app.route('/submit_result', methods=['POST'])
def store_result():
    if not request.json:
        abort(400)
    match_result = request.json
    enterer = match_result['who_entered']
    winner = match_result['winner']
    loser = match_result['loser']
    score = match_result['score']

    #Check if the player entered is valid
    players = ['brett', 'jwong']
    if is_player_valid(winner, players) == False:
        response = f"{winner} doesn't exist. Please enter a valid winner's username."
    #Check if the score entered is valid
    if is_score_valid(score) == False:
        response = f"{score} is not a valid score, get your act together and input it properly!"
    else:
        winner_score = get_winner_loser_score(score)['winner_score']
        loser_score = get_winner_loser_score(score)['loser_score']
        response = winner_score

    # else:
    #     response = f'Thanks, {enterer}, for submitting match result'

    return jsonify(response)


# @app.route('/')
# def index():
#     return render_template('index.html')

app.run(debug=True)
