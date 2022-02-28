import sqlite3
tuple1 = ('Back in Black' , 10)
tuple2 = ('Panzerkampf' , 19)
conn = sqlite3.connect('music.sqlite)')
cursor = conn.cursor()
cursor.execute('DROP TABLE  IF EXISTS Ages')
cursor.execute('CREATE TABLE Ages(name VARCHAR(128), age INTEGER)')


cursor.execute('INSERT INTO Ages(name , age) Values(?,?)', ('Chase' , 23))
cursor.execute('INSERT INTO Ages(name , age) Values(?,?)', ('Triniti', 32))
cursor.execute('INSERT INTO Ages(name , age) Values(?,?)', ('Nikodem' , 21))
cursor.execute('INSERT INTO Ages(name , age) Values(?,?)', ('Basile', 23))
cursor.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
cursor.close()
