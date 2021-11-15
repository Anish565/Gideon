import sqlite3
from sqlite3.dbapi2 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, createTableSQL):
    try:
        c = conn.cursor()
        c.execute(createTableSQL)
    except Error as e:
        print(e)


def create_contact(conn, contact):
    sql = '''INSERT INTO Contacts(name,number)
            VALUES(?,?)'''

    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()

    return cur.lastrowid

def retrieveContact(conn, name):
    cur = conn.cursor()
    sql = "SELECT * FROM contacts WHERE name = ?"
    name = (name,)
    cur.execute(sql,name)

    rows = cur.fetchall()
    for row in rows:
        print("+91" + str(row[2]))


# database = "/Users/pran/Desktop/Contacts.db"
database = "C:/Users/Anisn/Desktop/codes/Gideon/Contacts.db"
sql_create_table = """CREATE TABLE IF NOT EXISTS Contacts(
            id INTEGER PRIMARY KEY,
            name text NOT NULL,
            number INTEGER
); """

conn = create_connection(database)

if conn is not None:
    create_table(conn, sql_create_table)
else:
    print("Cannot Establish Connection.")


# name = input("Enter the name")
# num = int(input("Enter the number"))

# contact = (name,num)
# create_contact(conn,contact)

retrieveContact(conn, "Charan")