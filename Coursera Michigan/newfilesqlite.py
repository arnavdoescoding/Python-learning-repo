import sqlite3
conn = sqlite3.connect('assignment.sqlite')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (org TEXT , count INTEGER)')

fname = 'output.txt'
fhand = open(fname)
for org in fhand:
    cursor.execute('SELECT count FROM Counts WHERE org = ? ', (org , ))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts (org , count) VALUES(? , 1)', (org, ))
        conn.commit()
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
        conn.commit()

sqlstr = 'SELECT org , count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cursor.execute(sqlstr):
    print(str(row[0]) , row[1])

cursor.close()