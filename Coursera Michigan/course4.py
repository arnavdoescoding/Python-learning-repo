import sqlite3
tuple1 = ('Back in Black' , 10)
tuple2 = ('Panzerkampf' , 19)
conn = sqlite3.connect('music.sqlite)')
cursor = conn.cursor()
cursor.execute('DROP TABLE  IF EXISTS Tracks')
cursor.execute('CREATE TABLE Tracks(Title TEXT, Plays integer)')


cursor.execute('INSERT INTO Tracks(title , plays) Values(?,?)', tuple1)
cursor.execute('INSERT INTO Tracks(title , plays) Values(?,?)', tuple2)
conn.commit()

