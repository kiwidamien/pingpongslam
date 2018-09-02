import os
from flask import Flask, url_for, render_template, jsonify, request, abort

from make_app import app
from submit_request import store_result
from can_challenge import you_can_challenge

from leaderboard import pull_leaderboard

#  Homepage
@app.route('/')
def index():
    return render_template('index.html')


#  Leaderboard
@app.route('/leaderboard/')
def get_leaderboard():
    ranks = pull_leaderboard()
    #return jsonify(pull_leaderboard())

    return render_template('leaderboard.html', ranks=ranks)


#  Get top n from Leaderboard
@app.route('/api/leaderboard/top/<n>/')
def get_leaderboard_take_n_api(n):
    n= int(n)
    ranks = pull_leaderboard()[:n]
    return jsonify(ranks)

#  Get top n from Leaderboard
@app.route('/leaderboard/top/<n>/')
def get_leaderboard_take_n(n):
    n = int(n)
    ranks = pull_leaderboard()[:n]
    return render_template('leaderboard.html', ranks=ranks)


# Get matches for given user
@app.route('/username/<username>/')
def get_matches(username):
    matches = [{'date':'1/9/2018','score':'12-0','winner':'Jenn Wong','loser':'Brett','rank_of_user':'1'},
               {'date':'31/8/2018','score':'15-0','winner':'Jenn Wong','loser':'Brett','rank_of_user':'2'},
               {'date':'30/8/2018','score':'11-0','winner':'Jenn Wong','loser':'Brett','rank_of_user':'2'},
               {'date':'29/8/2018','score':'14-0','winner':'Jenn Wong','loser':'Brett','rank_of_user':'2'}]
    return render_template('raw_matches.html', matches=matches, username=username)


# Get most n recent matches for given user
@app.route('/api/<username>/recent/<n>/')
def get_recent_matches(username, n):
    pass


#  Get list of people to challenge
@app.route('/api/<username>/can_challenge/')
def get_list_can_challenge(username):
    pass

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
