import sqlite3

def connect():
    conn=sqlite3.connect("City.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS City (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(Latitude,Longitude,Type,Veg?Non-Veg):
    conn=sqlite3.connect("City.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO City VALUES (NULL,?,?,?,?)",(Latitude,Longitude,Type,Veg/Non-Veg))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("City.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM City")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Latitude="",Longitude="",Type="",Veg/Non-Veg=""):
    conn=sqlite3.connect("City.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM City WHERE Latitude=? OR Longitude=? OR Type=? OR Veg/Non-Veg=?", (Latitude,Longitude,Type,Veg/Non-Veg))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("City.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM City WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("City.db")
    cur=conn.cursor()
    cur.execute("UPDATE City SET Latitude=?, Longitude=?, Type=?, Veg/Non-Veg=? WHERE id=?",(Latitude,Longitude,Type,Veg/Non-Veg,id))
    conn.commit()
    conn.close()

connect()