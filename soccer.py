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

cur.execute("DROP TABLE IF EXISTS COUNTRY,PLAYERS,MATCH_RESULTS,PLAYER_CARD,PLAYER_ASSIST_GOALS")
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
                             IS_CAPTAIN BOOLEAN);"""
cur.execute(create_player_table_sql)
#run the player table sql query

db.close()
#closing database connection