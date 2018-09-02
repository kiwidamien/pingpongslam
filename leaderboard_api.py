from flask import Flask, abort, render_template, jsonify, request
from leaderboard import pull_leaderboard
import os

app = Flask('Pingpongslam')
@app.route('/api/leaderboard', methods=['GET'])
#print('yes')

def pull_leaderboard_api_call():
    print('called func')
    return jsonify(pull_leaderboard())

app.run(debug = True)
