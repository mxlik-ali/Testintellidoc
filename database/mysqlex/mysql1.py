import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "9870687802Am*",
    database = "mysqldb1"
)
cur = mydb.cursor()
# cur.execute("CREATE DATABASE mysqldb1") #creates a database
# cur.execute("SHOW DATABASES") #here it shows all the databases available
# for db in cur:
#     print(db)

# cur.execute("CREATE TABLE students(name TEXT,age INTEGER)")

cur.execute("SHOW TABLES") #here it shows all the tables available
for db in cur:
    print(db)