/* Queries  */
-- 1. rows 8
SELECT 
    name, club, country
FROM
    players
WHERE
    position = 'Midfielder' AND
    country = 'USA';

-- 2. rows 736
SELECT 
    name, club, country, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age
FROM
    players
WHERE
    is_captain = 1;

-- 3. rows 3
SELECT 
    country_name
FROM
    country
WHERE
    no_of_worldcup_won > 2;

-- 4. (24 rows returned) 
SELECT 
    country_name
FROM
    country
WHERE
    no_of_worldcup_won = 0;

--  5. 572 rows
SELECT p1.name, p1.country
FROM players p1
WHERE NOT EXISTS 
(SELECT *
FROM player_card p2
WHERE p2.player_id = p1.player_id);

--  6. 10 rows
SELECT 
    name, country
FROM
    players p1,
    player_card p2
WHERE
    p1.player_id = p2.player_id
        AND p2.no_of_red_cards IN (SELECT 
            MAX(no_of_red_cards)
        FROM
            player_card);

-- 7. 3 rows 
SELECT 
    name, country
FROM
    players p1,
    player_card p2
WHERE
    p1.player_id = p2.player_id
        AND p2.no_of_yellow_cards IN (SELECT 
            MAX(no_of_yellow_cards)
        FROM
            player_card);

-- 8.  rows 12
SELECT 
    host_city, COUNT(*) number_games
FROM
    match_results
GROUP BY host_city;

-- 9.   rows 2
select host_city from (
select host_city, count(*) games_played 
  from match_results 
group by host_city
) t123
where games_played in (select max(games_played) from (select host_city, count(*) games_played 
														from match_results 
													group by host_city) t321
						)							

-- 10. 32 rows with Brazil having 13 goals against team2  
select team1, count(team1) AS number_of_games_played_as_team1,sum(team1_score),sum(team2_score) 
from match_results 
group by team1;

-- 11 32 rows with Netherlands having 11 goals against team1
SELECT 
    team2, COUNT(team2) AS number_of_games_played_as_team2, SUM(team2_score), SUM(team1_score)
FROM
    match_results
GROUP BY team2;

-- 12. rows 128
create table t1 as(
select team1 country_name, count(team1) number_games,sum(team1_score) total_goals_for,sum(team2_score) total_goals_against
from match_results 
group by team1);

create table t2 as (
select team2 country_name, count(team2) number_games,sum(team2_score) total_goals_for,sum(team1_score) total_goals_against
from match_results 
group by team2);

create table t as
select * from t1
union
select * from t2;

create view team_summary as
select country_name AS CountryName,sum(number_games) AS NoOfGames, sum(total_goals_for) AS TotalGoalsFor,sum(total_goals_against) AS TotalGoalsAgainst
from t
group by CountryName
order by NoOfGames desc;

-- 13. rows 32
select CountryName, sum(NoOfGames) 
from team_summary
group by CountryName;

-- 14. rows 4
SELECT 
    CountryName
FROM
    (SELECT 
        CountryName, SUM(NoOfGames) games_played
    FROM
        team_summary
    GROUP BY CountryName) t2
WHERE
    games_played IN (SELECT 
            MAX(games_played)
        FROM
            (SELECT 
                CountryName, SUM(NoOfGames) games_played
            FROM
                team_summary
            GROUP BY CountryName) t1);
					   
-- 15  64 rows and no winning_team_score in negative 
SELECT 
    date_of_match, team1, team2,
    IF(team1_score > team2_score,
        team1,
        team2) winning_team,
    IF(team1_score > team2_score,
        team1_score - team2_score,
        team2_score - team1_score) goal_difference
FROM
    match_results;
	
--16. 5 rows returned 
(select * 
  from match_results
  where team1 = 'Argentina'
    and team1_score > team2_score)
union  
(select * 
  from match_results
  where team2 = 'Argentina'
    and team2_score > team1_score);
	
-- 17.  116 rows 
SELECT 
    p1.name, p1.country, p2.goals
FROM
    players p1,
    player_assists_goals p2
WHERE
    p1.player_id = p2.player_id
        AND p1.player_id IN (SELECT 
            player_id
        FROM
            player_assists_goals
        WHERE
            goals > 0)
ORDER BY p2.goals DESC;

/* Question 4 */
-- null constraint violation
INSERT INTO country VALUES(NULL,100,1,"Amith");
-- unique constraint violation
INSERT INTO country VALUES("Brazil",100,1,"Amith");
-- referential constraint violation
INSERT INTO players VALUES(1000,"Amith Hegde","Amith","Hegde","1991-03-01","China",175,"FIFA","Goalkeeper",100,1);

/*Question 5*/
DELETE FROM country WHERE country_name = "Brazil";

/*Question 6*/
-- 1.
INSERT INTO country VALUES("India",200,1,"Amith Hegde");
-- 2.
INSERT INTO players VALUES(38665,"Gaurav Kolekar","Gaurav","Kolekar","1990-05-17","India",175,"Mumbai FC","Goalkeeper",1,1);
-- 3.
INSERT INTO match_results VALUES(65,"2014-7-31","13:00:00","India","Brazil",2,1,"Estadio Nacional","Brasilia");
-- 4.
INSERT INTO player_card VALUES(38665,1,0);
-- 5.
INSERT INTO player_assists_goals VALUES(38665,1,1,1,90);


DELETE FROM player_assists_goals WHERE player_id = 38665;
DELETE FROM player_card WHERE player_id = 38665;
DELETE FROM match_results WHERE match_id = 65;
DELETE FROM players WHERE player_id = 38665;
DELETE FROM country WHERE country_name = "India";
