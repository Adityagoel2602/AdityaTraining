import sqlite3 as lite
con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT ,Price INT)")
    print("table cars created")
    cur.execute("INSERT INTO Cars VALUES(1,'AUDI',57566)")
    cur.execute("INSERT INTO Cars VALUES(2,'MERCEDES',57545)")
print("values in the table cars created")
