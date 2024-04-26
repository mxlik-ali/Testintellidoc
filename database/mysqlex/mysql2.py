import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "9870687802Am*",
    database = "mysqldb1"
)
cur = mydb.cursor()

# sqlFormula = "INSERT INTO students(name,age) VALUES (%s,%s)"
# students = [("Ali", 20),("Sagar", 21),("Sachin", 19),("Abhi", 20),("Nikunj", 21)]
# cur.executemany(sqlFormula,students) #here executemany makes the entire array of entries

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

mydb.commit()