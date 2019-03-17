import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Iamkira616",
	database = "badmintondb"
	)


my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE badmintondb")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
	#print(db)

#my_cursor.execute("CREATE TABLE players (name VARCHAR(255), country VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
	#print(table)

#sqlStuff = "INSERT INTO players (name, country, age) VALUES (%s, %s, %s)"
#record1 = ("Kento Momota", "Japan", 24)

#my_cursor.execute(sqlStuff, record1)
#mydb.commit()

#sqlStuff = "INSERT INTO players (name, country, age) VALUES (%s, %s, %s)"
#records = [("Lin Dan", "China", 34),
#	("Viktor Axelsen", "Denmark", 24),
#	("Chou Tien Chen", "Taiwan", 28),
#	("Son Wan Ho", "South Korea", 30),]

#my_cursor.executemany(sqlStuff, records)
#mydb.commit()

#my_cursor.execute("SELECT name FROM players")
#result = my_cursor.fetchall()
#for row in result:
#	print(row)

#my_cursor.execute("SELECT * FROM players WHERE name LIKE 'l%'")
#result = my_cursor.fetchall()
#for row in result:
#	print(row)

# LIMIT RESULTS
#my_cursor.execute("SELECT * FROM players ORDER BY age ASC")
#result = my_cursor.fetchall()
#for row in result:
#	print(row)

#DELETE RECORDS
#mysql = "DELETE FROM players WHERE user_id = #"
#my_cursor.execute(my_sql)
#mydb.commit()


