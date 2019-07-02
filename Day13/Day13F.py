import sqlite3 as lite
con=lite.connect('test.db')
def input_fun():
    a=int(input("Enter ID:"))
    b=input("Enter Name:")
    b="'"+b+"'"
    c=int(input("Enter Price:"))
    str1="INSERT INTO Cars VALUES({},{},{})".format(a,b,c)
    return str1
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT ,Price INT)")
    print("table cars created")
    cur.execute(input_fun())
print("values in table car inserted")
