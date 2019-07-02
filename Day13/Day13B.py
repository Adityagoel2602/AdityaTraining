import sqlite3
con=sqlite3.connect('test1.db')
cur=con.cursor()
cur.execute('SELECT SQLITE_VERSION()')
data=cur.fetchone()
print(" SQLite version",data)
