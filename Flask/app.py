import os
from flask import Flask, render_template, jsonify, request, abort

#  Initialization
app=Flask('PingPongApp')

#  Homepage
@app.route('/')
def homepage():
    return render_template('pingpong.html')


#  Leaderboard
@app.route('/api/leaderboard/')
def get_leaderboard():
    return render_template('leaderboard.html')


#  Get top n from Leaderboard
@app.route('/api/leaderboard/top/<n>/')
def get_leaderboard_take_n(n):
    pass


# Get matches for given user
@app.route('/api/<username>/')
def get_matches(username):
    pass


#  Get list of people to challenge
@app.route('/api/<username>/can_challenge/')
def get_list_can_challenge(username):
    return """
    <h1>Welcome to the app.</h1>

    Hi {}, here are the people you can challenge:
    """.format(username)


# Get most n recent matches for given user
@app.route('/api/<username>/recent/<n>/')
def get_recent_matches(username, n):
    pass



@app.route('/api/submit_result/', methods=['POST'])
def give_match_result():
    pass



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
