import sqlite3

def create():
    con = sqlite3.connect("studentsfees.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY,student TEXT,fees INTEGER)")
    con.commit()
    con.close()


def insert(student, fees):
    con = sqlite3.connect("studentsfees.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO info VALUES (NULL,?,?)", (student, fees))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("studentsfees.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM info")
    row = cursor.fetchall()
    return row


def search(student="", fees=""):
    con = sqlite3.connect("studentsfees.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM info WHERE student=? OR fees=?", (student, fees))
    row = cursor.fetchall()
    return row


def delete(id):
    con = sqlite3.connect("studentsfees.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM info WHERE id=?", (id,))
    con.commit()
    con.close()


def update(id, student, fees):
    con = sqlite3.connect("studentsfees.db")
    cursor = con.cursor()
    cursor.execute("UPDATE info SET student=?,fees=? WHERE id=?", (student, fees, id))
    con.commit()
    con.close()


create()