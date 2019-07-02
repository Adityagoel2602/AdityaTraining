import sqlite3 as lite
con=lite.connect('test.db')

with con:
    cur=con.cursor()
    cur.execute("SELECT * FROM training_data")
    rows=cur.fetchall()

print(rows)
print('-'*30)
for row in rows:
    print(row)

with con:
    cur=con.cursor()
    cur.execute("SELECT * FROM test_data")
    rows=cur.fetchall()

print(rows)
print('-'*30)
for row in rows:
    print(row)
