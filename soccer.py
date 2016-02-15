'''
This program is for CSE 5330: Database System project 1
Team:
Gaurav Vivek Kolekar
Amit Hegde
'''
import MySQLdb
#Importing MySQLdb library so that my python program can talk to the MYSQL database
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="password", db="SOCCER")
#connecting to the database
cur = db.cursor()
#creating a cursor object to excute queries on the database
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print "Database version:", str(data)
db.close()
#closing database connection