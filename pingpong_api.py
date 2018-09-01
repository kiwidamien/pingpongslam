import numpy as np
import pickle
import requests
import pandas as pd

test_match = {'winner': 'jwong', 'loser': 'brett', 'score': '21-3',
                    'date_of_match': '2018-08-31', 'who_entered': 'jwong', 'who_challenged': 'brett'}


#response = requests.get('http://127.0.0.1:5000/')
#print(response.text)

#response = requests.post('http://127.0.0.1:5000/submit_result',
# json=test_match)
#print(response.json())

# player_table = player

def is_player_valid(player, player_list):
    """Checks if the player exists in the players table"""
    return player in player_list

def is_score_valid(score):
    """Checks if the score is valid"""
    try:
        match_score = score.split('-')
        match_score = list(map(int, match_score))
        if len(match_score) != 2:
            print(len(match_score))
            return False
        elif max(match_score) < 21:
            print(match_score)
            return False
        elif max(match_score) - min(match_score) < 2:
            print(max(match_score) - min(match_score))
            return False
        else:
            return True
    except:
        print('exception')
        return False

def get_winner_loser_score(score):
    """Returns a tuple of winner, loser scores"""
    match_score = score.split('-')
    match_score = list(map(int, match_score))
    score_winner = max(match_score)
    score_loser = min(match_score)
    return {'score_winner': score_winner, 'score_loser': score_loser}



# if __name__ == '__main__':
#     print(test_match)
