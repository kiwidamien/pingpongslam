import psycopg2 as pg
import os
from .get_db_connection import get_connection

def pull_leaderboard():

    conn = get_connection()
    #print('worked')

    user_dict = {}
    cursor = conn.cursor()
    record_query = """
    WITH win_record as (
        SELECT player,
            SUM(CASE WHEN outcome='winner' THEN 1 ELSE 0 END) as num_wins,
            SUM(CASE WHEN outcome='loser' THEN 1 ELSE 0 END) as num_loss
        FROM player_match GROUP BY player),
        player_rank as (
            SELECT player, match_id, rank() over (partition by player order by match_id desc) as window_rank
            FROM player_match
        )

    SELECT player.Name, win_record.num_wins, win_record.num_loss, player_rank.match_id, player_match.rank,  window_rank, player.Rank
        FROM player
        LEFT JOIN win_record ON player.Name=win_record.player
        LEFT JOIN player_rank ON player.Name=player_rank.player
        LEFT JOIN player_match ON (player.Name=player_match.player AND player_rank.match_id=player_match.match_id)
        WHERE window_rank <= 2 OR window_rank IS NULL
        ORDER BY player_match.rank, window_rank;
    """
    cursor.execute(record_query)
    user_dict = {}

    full_results = cursor.fetchall()
    for result in full_results:
        id, num_wins, num_loss, match_id, rank, window_rank, initial_rank = result
        if id in user_dict:
            user_dict[id]['prev_rank'] = rank
        elif (num_wins is None or num_loss is None):
            user_dict[id] = {
                'record': '0-0',
                'rank': initial_rank
            }
        else:
            user_dict[id] = {
                'record' : f'{num_wins}-{num_loss}',
                'rank': rank
            }

    list_of_users = []
    for result in full_results:
        id, num_wins, num_loss, match_id, rank, window_rank, initial_rank = result
        if window_rank == 2:
            continue
        list_of_users.append({
            'id': id,
            'record': user_dict[id]['record'],
            'rank': user_dict[id].get('rank', initial_rank),
            'previous_rank': user_dict[id].get('prev_rank', initial_rank)
        })
    print('this is the list')
    newlist = sorted(list_of_users, key=lambda k: k['rank'])
    conn.close()
    return(newlist)


if __name__ == '__main__':
    pull_leaderboard()
