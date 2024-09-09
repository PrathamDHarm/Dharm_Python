import sqlite3

def sq():
    con=sqlite3.connect(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\python\demo1.db")
    cur=con.cursor()

    cur.execute("create table stude(id int primary key,name text,age int)")

    con.commit()

    cur.execute("insert into stude values(101,'Sai',18)")
    cur.execute("insert into stude values(102,'Dharm',17)")
    cur.execute("insert into stude values(103,'Govind',18)")
    cur.execute("insert into stude values(104,'Prathamesh',20)")
    cur.execute("insert into stude values(105,'Ajay',20)")
    

    con.commit()
     
    cur.execute('select * from stud')

    cur.fetchall()


sq()
 
