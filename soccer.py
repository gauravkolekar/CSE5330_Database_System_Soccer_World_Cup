'''
This program is for CSE 5330: Database System project 1
Team:
Gaurav Vivek Kolekar
Amit Hegde
'''

import csv
#Importing csv to read the dataset
from configuration import database_configurations as db

cur = db.cursor()
#creating a cursor object to excute queries on the database

cur.execute("SELECT VERSION()")
#query to find out the database version

data = cur.fetchone()
print "Database version: ",str(data)
#printing the database version

csv_file_handler = open("Country.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

row_affected = 0
for row in csv_reader:
    #print row
    data_Country_Name = row[0]
    data_population = float(row[1])
    data_no_of_worldcup_won = int(row[2])
    data_manager = row[3]
    #print data_Country_Name,data_population,data_no_of_worldcup_won,data_manager
    sql_insert_query = "INSERT INTO COUNTRY VALUES(%s,%d,%d,%s)"%(data_Country_Name,data_population,data_no_of_worldcup_won,data_manager)
    cur.execute(sql_insert_query)
    row_affected = row_affected + 1
db.commit()
print  "rows affected:",str(row_affected)
print "COUNTRY table populated ..."
#populated the COUNTRY table

csv_file_handler = open("Players.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

row_affected = 0
for row in csv_reader:
    #print  row
    data_player_id = int(row[0])
    data_name = row[1]
    data_fname = row[2]
    data_lname = row[3]
    data_dob = row[4]
    data_country = row[5]
    data_height = int(row[6])
    data_club = row[7]
    data_position = row[8]
    data_caps_for_country = int(row[9])
    data_is_captain = row[10]
    #print data_player_id,data_name,data_fname,data_lname,data_dob,data_country,data_height,data_club,data_position,data_caps_for_country,data_is_captain
    sql_insert_query = "INSERT INTO PLAYERS VALUES(%d,%s,%s,%s,%s,%s,%d,%s,%s,%d,%s)"%(data_player_id,data_name,data_fname,data_lname,data_dob,data_country,data_height,data_club,data_position,data_caps_for_country,data_is_captain)
    cur.execute(sql_insert_query)
    row_affected = row_affected + 1
db.commit()
print  "rows affected:",str(row_affected)
print "PLAYERS table populated ..."
#populated the PLAYERS table

csv_file_handler = open("Match_results.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

row_affected = 0
for row in csv_reader:
    #print  row
    data_match_id = int(row[0])
    data_date_of_match = row[1]
    data_start_time_of_match = row[2]
    data_team1 = row[3]
    data_team2 = row[4]
    data_team1_score = int(row[5])
    data_team2_score = int(row[6])
    data_stadium_name = row[7]
    data_host_city = row[8]
    #print data_match_id,data_date_of_match,data_start_time_of_match,data_team1,data_team2,data_team1_score,data_team2_score,data_stadium_name,data_host_city
    sql_insert_query = "INSERT INTO MATCH_RESULTS VALUES(%d,%s,%s,%s,%s,%d,%d,%s,%s)"%(data_match_id,data_date_of_match,data_start_time_of_match,data_team1,data_team2,data_team1_score,data_team2_score,data_stadium_name,data_host_city)
    cur.execute(sql_insert_query)
    row_affected = row_affected + 1
db.commit()
print  "rows affected:",str(row_affected)
print "MATCH_RESULTS table populated ..."
#populated the MATCH_RESULTS table

csv_file_handler = open("Player_Cards.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

row_affected = 0
for row in csv_reader:
    #print row
    data_player_id = int(row[0])
    data_no_of_yellow_card = int(row[1])
    data_no_of_red_card = int(row[2])
    #print data_player_id,data_no_of_yellow_card,data_no_of_red_card
    sql_insert_query = "INSERT INTO PLAYER_CARD VALUES(%d,%d,%d)"%(data_player_id,data_no_of_yellow_card,data_no_of_red_card)
    cur.execute(sql_insert_query)
    row_affected = row_affected + 1
db.commit()
print  "rows affected:",str(row_affected)
print "PLAYER_CARDS table populated ..."
#populated the PLAYER_CARD table

csv_file_handler = open("Player_Assists_Goals.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

row_affected = 0
for row in csv_reader:
    #print row
    data_player_id = int(row[0])
    data_no_of_matches = int(row[1])
    data_goals = int(row[2])
    data_assists = int(row[3])
    data_minutes_played = int(row[4])
    #print data_player_id, data_no_of_matches,data_goals,data_assists,data_minutes_played
    sql_insert_query = "INSERT INTO PLAYER_ASSISTS_GOALS VALUES(%d,%d,%d,%d,%d)"%(data_player_id, data_no_of_matches,data_goals,data_assists,data_minutes_played)
    cur.execute(sql_insert_query)
    row_affected = row_affected + 1
db.commit()
print  "rows affected:",str(row_affected)
print "PLAYER_ASSISTS_GOALS table populated ..."
#populated the COUNTRY table

db.close()
#closing database connection