import random
import sqlite3 as lite

def str_float(x):
    for i in range(0,len(x)-1):
        x[i] = float(x[i])
    return tuple(x)

training_data = []
test_data = []
for line in open("iris.txt"):
    temp = line[:-1].split(",")
    if random.random() <= 0.8:
        training_data.append(str_float(temp))
    else:
        test_data.append(str_float(temp))

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS training_data")
    cur.execute("DROP TABLE IF EXISTS test_data")
    cur.execute('CREATE TABLE training_data(x1 INT, y1 INT,  x2 INT,  y2 INT, Name TEXT)')
    cur.execute('CREATE TABLE test_data(x1 INT, y1 INT,  x2 INT,  y2 INT, Name TEXT)')
    cur.executemany("INSERT INTO training_data Values(?,?,?,?,?)",training_data)
    cur.executemany("INSERT INTO test_data Values(?,?,?,?,?)",test_data)
print("Data inserted successfully")
