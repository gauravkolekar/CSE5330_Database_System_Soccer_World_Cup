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
    print data_Country_Name,data_population,data_no_of_worldcup_won,data_manager
    sql_insert_query = "INSERT INTO COUNTRY VALUES(%s,%d,%d,%s)"%(data_Country_Name,data_population,data_no_of_worldcup_won,data_manager)
    cur.execute(sql_insert_query)
db.commit()
db.close()
#closing database connection