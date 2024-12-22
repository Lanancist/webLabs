import sqlite3 as sql
from User import *

class DB:
    def __init__(self):
        with sql.connect('DataBase.db') as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Clients (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            info TEXT
                            );''')

    def get_user_by_id(self, user_id:int) -> object:
        with sql.connect('DataBase.db') as con:
            cur = con.cursor()

            cur.execute("SELECT name, info FROM Clients WHERE id = ?", (user_id,))

            dat = cur.fetchone()

            if dat == None:
                raise Exception()
            return User(dat[0], dat[1])

    def add_user(self, user_name:str, user_info: str) -> int:
        with sql.connect('DataBase.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Clients (name, info) VALUES (?, ?)", (user_name, user_info))

            return cur.lastrowid
