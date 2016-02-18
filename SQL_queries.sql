/* Queries  */
-- 1.     returns 249 rows
SELECT 
    name1, club, country
FROM
    players
WHERE
    position1 = 'Midfielder';

-- 2
SELECT 
    name1,
    club,
    country,
    TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age
FROM
    players
WHERE
    is_captain = 1;

-- 3. 
SELECT 
    country_name
FROM
    country
WHERE
    no_world_cup_won > 2;

-- 4. (24 rows returned) 
SELECT 
    country_name
FROM
    country
WHERE
    no_of_worldcup_won = 0;

--  5. empty set
SELECT 
    name1, country
FROM
    players p1,
    player_card p2
WHERE
    p1.player_id = p2.player_id
        AND p2.no_of_yellow_cards = 0
        AND p2.no_of_red_cards = 0;

--  6. 9 rows
SELECT 
    name1, country
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
    name1, country
FROM
    players p1,
    player_card p2
WHERE
    p1.player_id = p2.player_id
        AND p2.no_of_yellow_cards IN (SELECT 
            MAX(no_of_yellow_cards)
        FROM
            player_card);

-- 8.  
SELECT 
    host_city, COUNT(*) number_games
FROM
    match_results
GROUP BY host_city;

-- 9.   
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
select team1, count(team1),sum(team1_score),sum(team2_score) 
from match_results 
group by team1;

SELECT 
    team1, team1_score, team2_score
FROM
    match_results
GROUP BY team1 , team1_score , team2_score;

-- 11 32 rows with Netherlands having 11 goals against team1
SELECT 
    team2, COUNT(team2), SUM(team2_score), SUM(team1_score)
FROM
    match_results
GROUP BY team2;

-- 12  

-- incorrect once
create view team_summary as
select country_name, number_games, total_goals_for, total_goals_against from
(select team1 country_name, count(team1) number_games,sum(team1_score) total_goals_for,sum(team2_score) total_goals_against
from match_results 
group by team1
union
select team2 country_name, count(team2) number_games,sum(team2_score) total_goals_for,sum(team1_score) total_goals_against
from match_results 
group by team2) t_union
order by number_games desc;

--  correct one
create or replace view team_summary1 as
select country_name,sum(total_goals_for), sum(total_goals_against),sum(number_games) number_games from
(select team1 country_name, count(team1) number_games,sum(team1_score) total_goals_for,sum(team2_score) total_goals_against
from match_results 
group by team1
union
select team2 country_name, count(team2) number_games,sum(team2_score) total_goals_for,sum(team1_score) total_goals_against
from match_results 
group by team2) t_union
group by country_name
order by number_games desc

-- 13   
select country_name, sum(number_games) from team_summary group by country_name;

-- 14   
SELECT 
    country_name
FROM
    (SELECT 
        country_name, SUM(number_games) games_played
    FROM
        team_summary
    GROUP BY country_name) t2
WHERE
    games_played IN (SELECT 
            MAX(games_played)
        FROM
            (SELECT 
                country_name, SUM(number_games) games_played
            FROM
                team_summary
            GROUP BY country_name) t1);
					   
-- 17.  116 rows 
SELECT 
    p1.name1, p1.country, p2.goals
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

-- 169 rows  useless
SELECT 
    p1.name1, p1.country, p2.goals
FROM
    players p1,
    player_assists_goals p2
WHERE
    p1.player_id = p2.player_id
GROUP BY p1.name1 , p1.country , p2.goals
HAVING COUNT(p2.goals) > 0
ORDER BY p2.goals DESC;
					   