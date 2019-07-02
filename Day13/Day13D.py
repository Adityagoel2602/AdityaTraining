import sqlite3 as lite

cars=(
    (1,'Audi',56789),
    (2,'Mercedes',56432),
    (3,'Skoda',54678),
    (4,'Volvo',35436),
    (5,'Bentley',35566),
    (6,'Hammer',56784),
    (7,'Volkswagen',22345)
)

con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT ,Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?,?,?)",cars)
 
