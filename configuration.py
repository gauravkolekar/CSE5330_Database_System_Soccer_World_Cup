import MySQLdb
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="password", db="SOCCER")
#creating a configuration file which can be changed as per the user of the program