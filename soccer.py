'''
This program is for CSE 5330: Database System project 1
Team:
Gaurav Vivek Kolekar
Amit Hegde
'''
import MySQLdb
#Importing MySQLdb library so that my python program can talk to the MYSQL database
import warnings
warnings.filterwarnings('ignore','Unknown table.*')
#MySQLdb throws warning and halts program when it tries to drop table that doesn't exsist, this helps us to supress those warnings
import csv

db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="password", db="SOCCER")
#connecting to the database

cur = db.cursor()
#creating a cursor object to excute queries on the database

cur.execute("SELECT VERSION()")
#query to find out the database version

data = cur.fetchone()
print "Database version: ",str(data)
#printing the database version

cur.execute("DROP TABLE IF EXISTS PLAYER_ASSIST_GOALS,PLAYER_CARD,MATCH_RESULTS,PLAYERS,COUNTRY;")
#dropping table if they exsist to start fresh

create_country_table_sql = """CREATE TABLE COUNTRY(
                              Country_Name VARCHAR(20) NOT NULL,
                              Population DECIMAL(10,2),
                              No_of_Worldcup_won INTEGER,
                              Manager VARCHAR(20),
                              PRIMARY KEY(Country_Name));"""
cur.execute(create_country_table_sql)
#run the country table create sql command

create_player_table_sql = """CREATE TABLE PLAYERS(
                             Player_id INTEGER NOT NULL,
                             Name VARCHAR(40),
                             Fname VARCHAR(20),
                             Lname VARCHAR(35),
                             DOB DATE,
                             Country VARCHAR(20),
                             Height INTEGER,
                             Club VARCHAR(20),
                             Position VARCHAR(10),
                             Caps_for_Country INTEGER,
                             IS_CAPTAIN BOOLEAN,
                             PRIMARY KEY(Player_id));"""
cur.execute(create_player_table_sql)
#run the player table sql query

create_match_results_table_sql = """CREATE TABLE MATCH_RESULTS(
                                    Match_id INTEGER NOT NULL,
                                    Date_of_Match DATE,
                                    Start_Time_Of_Match TIME,
                                    Team1 VARCHAR(25),
                                    Team2 VARCHAR(25),
                                    Team1_score INTEGER,
                                    Team2_score INTEGER,
                                    Stadium_Name VARCHAR(35),
                                    Host_City VARCHAR(20),
                                    PRIMARY KEY(Match_id));"""
cur.execute(create_match_results_table_sql)
#run the match_result sql query

create_player_card_table_sql = """CREATE TABLE PLAYER_CARD(
                                  Player_id INTEGER NOT NULL,
                                  Yellow_Card INTEGER,
                                  Red_Cards INTEGER,
                                  PRIMARY KEY(Player_id));"""
cur.execute(create_player_card_table_sql)
#run the player_card sql query

create_player_assists_goals = """CREATE TABLE PLAYER_ASSIST_GOALS(
                                 Player_id INTEGER NOT NULL,
                                 No_of_Matches INTEGER,
                                 Goals INTEGER,
                                 Assists INTEGER,
                                 PRIMARY KEY(Player_id));"""
cur.execute(create_player_assists_goals)
#run the player_assist_goals sql qery

add_foreign_Players_sql = """ALTER TABLE PLAYERS
                             ADD FOREIGN KEY(Country)
                             REFERENCES COUNTRY(Country_Name);"""
cur.execute(add_foreign_Players_sql)
#adding foreign key to player

add_foreign_match_result_sql = """ALTER TABLE MATCH_RESULTS
                                  ADD FOREIGN KEY (Team1)
                                  REFERENCES COUNTRY(Country_Name),
                                  ADD FOREIGN KEY (Team2)
                                  REFERENCES COUNTRY(Country_Name);"""
cur.execute(add_foreign_match_result_sql)
#adding the foreign key to match result table

add_foreign_key_player_card_sql = """ALTER TABLE PLAYER_CARD
                                     ADD FOREIGN KEY (Player_id)
                                     REFERENCES PLAYERS(Player_id);"""
cur.execute(add_foreign_key_player_card_sql)
#adding the foriegn key to player_card table

add_foreign_key_player_assist_goals_sql = """ALTER TABLE PLAYER_ASSIST_GOALS
                                             ADD FOREIGN KEY (Player_id)
                                             REFERENCES PLAYERS(Player_id);"""
cur.execute(add_foreign_key_player_assist_goals_sql)
#adding the foriegn key to PLAYER_ASSIST_GOALS table



db.close()
#closing database connection