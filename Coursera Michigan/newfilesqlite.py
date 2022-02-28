import sqlite3
conn = sqlite3.connect('assignment.sqlite')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (email TEXT , count INTEGER)')

fname = 'mbox.txt'
fhand = open(fname)
for line in fhand:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    email = pieces[1]
    cursor.execute('SELECT count FROM Counts WHERE email = ? ', (email , ))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts (email , count) VALUES(? , 1)', (email, ))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    conn.commit()

sqlstr = 'SELECT email , count FROM Counts ORDER BY count DISC LIMIT 10'
for row in cursor.execute(sqlstr):
    print(str(row[0] , row[1]))

cursor.close()