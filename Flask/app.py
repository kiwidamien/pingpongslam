import os
from flask import Flask, render_template, jsonify, request, abort

#  Initialization
app=Flask('PingPongApp')

#  Homepage
@app.route('/')
def homepage():
    return render_template('pingpong.html')


#  Leaderboard
@app.route('/leaderboard/')
def get_leaderboard():
    ranks = [{'id': 'Jenn Wong', 'record': '150-0', 'previous_rank': '2'},
             {'id': 'Auste M.', 'record': '22-4', 'previous_rank': '5'},
             {'id': 'Harmeet Hora', 'record': '50-5', 'previous_rank': '3'},
             {'id': 'Ilan M.', 'record': '10-1', 'previous_rank': '1'}]
    return render_template('leaderboard.html', ranks=ranks)


#  Get top n from Leaderboard
@app.route('/leaderboard/top/<n>/')
def get_leaderboard_take_n(n):
    pass


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



@app.route('/api/submit_result/', methods=['POST'])
def give_match_result():
    pass



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
