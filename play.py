import sqlite3

database = 'speech.sqlite'



conn = sqlite3.connect(database)
cur = conn.cursor()

cur.execute('SELECT speech FROM Speeches')

for row in cur:
    print(cur)