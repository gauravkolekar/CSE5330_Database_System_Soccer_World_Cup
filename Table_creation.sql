use db1;


CREATE TABLE country(
 country_name       VARCHAR(20)
,population         DECIMAL(10,2)
,no_of_worldcup_won INT
,manager            VARCHAR(20)
,PRIMARY KEY(country_name)
);


CREATE TABLE players
(
 player_id int
,name VARCHAR(40)
,fname VARCHAR(20)
,lname VARCHAR(35)
,dob DATE  
,country VARCHAR(20)
,height INT
,club VARCHAR(30)
,position VARCHAR(10)
,caps_for_country INT
,is_captain BOOLEAN
,PRIMARY KEY(player_id)
,FOREIGN KEY(country) REFERENCES country(country_name)
);

CREATE TABLE match_results
(
 match_id int
,date_of_match DATE
,start_time_of_match TIME
,team1 VARCHAR(20)
,team2 VARCHAR(20)
,team1_score INT
,team2_score INT 
,stadium_name VARCHAR(35)
,host_city VARCHAR(20)
,PRIMARY KEY(match_id)
,FOREIGN KEY(team1) REFERENCES country(country_name)
,FOREIGN KEY(team2) REFERENCES country(country_name)
);

CREATE TABLE player_card
(
 player_id INT
,no_of_yellow_cards INT
,no_of_red_cards INT
,PRIMARY KEY(player_id)
,FOREIGN KEY(player_id) REFERENCES players(player_id)
);

CREATE TABLE player_assists_goals
(
 player_id INT	
,no_of_matches INT
,goals INT
,assists INT
,minutes_played INT
,PRIMARY KEY(player_id)
,FOREIGN KEY(player_id) REFERENCES players(player_id)
);