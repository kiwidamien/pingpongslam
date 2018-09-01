test_match = {'winner': 'jwong', 'loser': 'brett', 'score': '21-3',
                    'date_of_match': '2018-08-31', 'who_entered': 'jwong', 'who_challenged': 'brett'}

def is_player_valid(player, player_list):
    """Checks if the player exists in the players table"""
    return player in player_list

def is_date_valid(date):
    """Checks if the date is valid"""
    try:
        year, month, day = date.split('-')
        if int(year) not in range(2018, 2023):
            return False
        elif int(month) not in range(1, 13):
            return False
        elif int(day) not in range(1, 32):
            return False
        else:
            return True
    except:
        print('exception')
        return False

def is_challenger_valid(challenger, winner, loser):
    """Checks if the challenger is one of the players"""
    if challenger != winner and challenger != loser:
        return False
    else:
        return True

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
        elif min(match_score) < 20 and max(match_score) > 21:
            return False
        elif min(match_score) >= 20 and max(match_score) - min(match_score) != 2:
            return False            
        elif max(match_score) - min(match_score) < 2:
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

def get_prev_rank(player, leaderboard):
    """Retrievs the rank of the player"""
    player_rank = 0

    for row in leaderboard:
        if row['id'] == player:
            player_rank = int(row['previous_rank'])
        else:
            pass
    return player_rank

# if __name__ == '__main__':
#     print(test_match)
