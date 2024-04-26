import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Count')
# cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter the file name ')
with open(fname,'r') as f:
    for lines in f:
        if not lines.startswith('From'):
            continue
        pieces = lines.split()
        email = pieces[1]
        cur.execute('SELECT count from Counts Where email=?',(email,))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO Counts(email,count) VALUES(?,1)',(email,))
        else:
            cur.execute('UPDATE Counts SET count = count+1 where email = ?', (email,))
conn.commit()

sqlstr = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()