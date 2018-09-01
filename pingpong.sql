CREATE DATABASE pingpong;

\connect pingpong;

CREATE TABLE player(
  Rank INT,
  Name TEXT,
);

CREATE TABLE match(
  Match_ID int NOT NULL AUTO_INCREMENT,
  Winner TEXT,
  Loser TEXT,
  Score_winner INT,
  Score_loser INT,
  Match_date DATE,
  Who_entered TEXT,
  Who_challenged TEXT,
  Win_rank INT,
  Lose_rank INT,
  Entered_time DATETIME,
  PRIMARY KEY (Match_ID)
  
);


/* from the view, we want to have rows of people, and the columns 

*/
CREATE VIEW player_match(
	with lost_matches as (
		select Loser as user, Score_loser as score, Lose_rank as rank, 'loser' as outcome 
		from match
		
	)
	,
	with win_matches as (
		select Winner as user, Score_winner as score, Win_rank as rank, 'winner' as outcome
		from match
	)
  select *
  from lost_matches
  union
  select * 
  from win_matches
  order by match_id desc; 

);


\copy player FROM 'player_table.csv' DELIMITER ',' CSV HEADER;
\copy match FROM 'match_data.csv' DELIMITER ',' CSV HEADER;



