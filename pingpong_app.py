from flask import Flask, abort, render_template, jsonify, request
import psycopg2
from pingpong_api import *

#Connect to the database and create a cursor
conn = psycopg2.connect(dbname="pingpong", user="auste_m")
cursor = conn.cursor()

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
        cursor.execute("""SELECT MAX(match_id) FROM match_result""")
        last_id = cursor.fetchone()[0]
        new_id = last_id + 1
        score_winner = get_winner_loser_score(score)['score_winner']
        score_loser = get_winner_loser_score(score)['score_loser']
        insert_scores_query = """INSERT INTO match_result(match_id, score_winner, score_loser)
                                    VALUES ({0}, {1}, {2});""".format(new_id, score_winner, score_loser)
        cursor.execute(insert_scores_query)
        conn.commit()
        response = f'Thanks, {enterer}, for submitting match result'

    return jsonify(response)


# @app.route('/')
# def index():
#     return render_template('index.html')

app.run(debug=True)
