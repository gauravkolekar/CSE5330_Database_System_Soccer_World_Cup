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

for row in csv_reader:
    #print row
    data_Country_Name = row[0]
    data_population = float(row[1])
    data_no_of_worldcup_won = int(row[2])
    data_manager = row[3]
    #print data_Country_Name,data_population,data_no_of_worldcup_won,data_manager
    sql_insert_query = "INSERT INTO COUNTRY VALUES(%s,%d,%d,%s)"%(data_Country_Name,data_population,data_no_of_worldcup_won,data_manager)
    cur.execute(sql_insert_query)
db.commit()
print "COUNTRY table populated ..."
#populated the COUNTRY table

csv_file_handler = open("Players.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

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
    data_is_captain = bool(row[10])
    #print data_player_id,data_name,data_fname,data_lname,data_dob,data_country,data_height,data_club,data_position,data_caps_for_country,data_is_captain
    sql_insert_query = "INSERT INTO PLAYERS VALUES(%d,%s,%s,%s,%s,%s,%d,%s,%s,%d,%d)"%(data_player_id,data_name,data_fname,data_lname,data_dob,data_country,data_height,data_club,data_position,data_caps_for_country,data_is_captain)
    cur.execute(sql_insert_query)
db.commit()
print "PLAYERS table populated ..."
#populated the PLAYERS table

csv_file_handler = open("Match_results.csv","rb")
csv_reader = csv.reader(csv_file_handler.read().strip().splitlines())

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
db.commit()
print "MATCH_RESULTS table populated ..."
#populated the MATCH_RESULTS table
db.close()
#closing database connection