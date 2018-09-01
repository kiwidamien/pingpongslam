DROP DATABASE pingpong;

CREATE DATABASE pingpong;

\connect pingpong;

CREATE TABLE player(
  Rank INT,
  Name TEXT
);

CREATE TABLE match_result(
  Match_ID SERIAL PRIMARY KEY,
  Winner TEXT,
  Loser TEXT,
  Score_winner INT,
  Score_loser INT,
  Match_date DATE,
  Who_entered TEXT,
  Who_challenged TEXT,
  Win_rank INT,
  Lose_rank INT,
  Entered_time TIMESTAMP
  
);


/* from the view, we want to have rows of people, and the columns 

*/
CREATE VIEW player_match AS (
	with lost_matches as (
		select Match_ID, Loser as user, Score_loser as score, Lose_rank as rank, 'loser' as outcome 
		from match_result
		
	)
	,
	win_matches as (
		select Match_ID, Winner as user, Score_winner as score, Win_rank as rank, 'winner' as outcome
		from match_result
	)
  select *
  from lost_matches
  union
  select * 
  from win_matches
  order by Match_ID desc 

);


\copy player FROM 'player_table.csv' DELIMITER ',' CSV HEADER;
\copy match_result FROM 'match_data.csv' DELIMITER ',' CSV HEADER;



