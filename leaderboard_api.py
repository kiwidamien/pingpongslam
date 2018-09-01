from flask import Flask, abort, render_template, jsonify, request
import psycopg2 as pg
import pandas.io.sql as pd_sql
import pandas as pd
import os

connection_args = {
    'host': 'localhost',
    'user': os.environ['USER'],
    'dbname': 'pingpong',
}

connection = pg.connect(**connection_args)

@app.route('/api/leaderboard', methods=['GET'])
def pull_leaderboard():
    user_dict = {}
    cursor = connection.cursor()
    record_query = 'SELECT player, \
    SUM(CASE WHEN outcome='winner' THEN 1 ELSE 0 END) as num_wins, \
    SUM(CASE WHEN outcome='loser' THEN 1 ELSE 0 END) as num_loss \
    FROM player_match GROUP BY player;'
    cursor.execute(record_query)
    ranks = []
    for result in cursor:
        user_dict['id'] = result[0]
        user_dict['record'] = result[1] + '-' + result[2]
        ranks.append(user_dict)

    rank_query = 'SELECT player, max(match_id), max(rank) \
    from player_match \
    group by player;'

    cursor.execute(rank_query)
    rank_dict= {}
    ranks2 = []
    for result in cursor:
        # now i have to use the rank to order then in the rank list
        # this query returns 3 things: player, latest_match, ranks
        rank_dict['id'] = result [0]
        rank_dict['rank'] = result[2]
        dict_search = next((item for item in rank if user_dict["id"] == result[0]))
        dict_search = dict_search.update(rank_dict)
        ranks2.append(dict_search)

    prev_rank_query = 'WITH prev_rank as (select player, match_id, rank() \
    over (partition by player order by match_id desc) as window_rank \
    from player_match) select prev_rank.player, prev_rank.match_id, prev_rank.window_rank, player_match.rank \
    from player_match left join prev_rank  on \
    player_match.match_id = prev_rank.match_id and player_match.player = prev_rank.player \
    where window_rank <=2;'

    rank3 = []

    cursor.execute(prev_rank_query)
    for result in cursor:
        prev_rank_dict['id'] = result [0]
        prev_rank_dict['previous_rank'] = result[3]
        dict_search = next((item for item in rank2 if user_dict["id"] == result[0]))
        dict_search = dict_search.update(prev_rank_dict)
        ranks3.append(dict_search)

    final_list = sorted(rank3, key=lambda k: k['rank'])

    return final_list
