from flask import Flask, abort, render_template, jsonify, request
import datetime as dt
import psycopg2
from pingpong_api import *
from make_app import app

@app.route('/api/submit_result', methods=['POST'])
def store_result():
    #Connect to the database and create a cursor
    conn = psycopg2.connect(dbname="pingpong", user="tarekbarnes")
    cursor = conn.cursor()

    if not request.json:
        abort(400)

    print(request.json)
    match_result = request.json
    winner = match_result['winner']
    loser = match_result['loser']
    score = match_result['score']
    enterer = match_result['who_entered']
    match_date = match_result['match_date']
    challenger = match_result['who_challenged']
    entered_time = dt.datetime.now()

    #Check if the players entered are valid
    if is_player_valid(winner) == False:
        response = f"{winner} doesn't exist. Please enter a valid winner's username."
        abort(403)
    elif is_player_valid(loser) == False:
        response = f"{loser} doesn't exist. Please enter a valid loser's username."
        abort(403)
    #Check if the score entered is valid
    elif is_score_valid(score) == False:
        response = f"{score} is not a valid score, get your act together and input it properly!"
        abort(400)
    #Check if the date entered is valid
    elif is_date_valid(match_date) == False:
        response = f'{match_date} is not valid. Please enter a valid match date.'
        abort(400)
    #Check if the challenger is one of the players
    elif is_challenger_valid(challenger, winner, loser) == False:
        response = f'The challenger must be one of the players.'
        abort(400)
    else:
        cursor.execute("""SELECT MAX(match_id) FROM match_result""")
        last_id = cursor.fetchone()[0]
        new_id = last_id + 1
        score_winner = get_winner_loser_score(score)['score_winner']
        score_loser = get_winner_loser_score(score)['score_loser']
        # leaderboard = pull_leaderboard()

        #WILL HAVE TO BE REPLACED BY JENMEENT'S FUNCTION FOR LEADERBOARD
        leaderboard = [{'id':'jwong','record':'52-0','previous_rank':'1'},
                           {'id':'brett','record':'26-7','previous_rank':'2'},
                           {'id':'damien','record':'24-3','previous_rank':'3'}]
        winner_rank = get_prev_rank(winner, leaderboard)
        loser_rank = get_prev_rank(loser, leaderboard)

        insert_result = """INSERT INTO match_result(match_id, winner, loser, score_winner, score_loser,
                                                            match_date, who_entered, who_challenged,
                                                            win_rank, lose_rank, entered_time)
                                 VALUES ({0}, '{1}', '{2}', {3}, {4}, '{5}', '{6}', '{7}', {8}, {9}, '{10}')
                                                            ;""".format(new_id, winner, loser, score_winner, score_loser,
                                                                            match_date, enterer, challenger, winner_rank,
                                                                            loser_rank, entered_time)
        cursor.execute(insert_result)
        conn.commit()
        if enterer == winner:
            response = f'Congrats, keep it up! Thanks for submitting the result.' #u"\U0001f44d"
        elif enterer == loser:
            response = f'Woah woah...thanks for submitting the result, better luck next time.' #u"\U0001F44E"
        else:
            response = f'Thank you for submitting match result, {enterer}.' #u"\U0001F609"

        conn.close()

    return jsonify(response)
