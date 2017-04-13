import sqlite3 #eventually replace with psyco
#import psycopg2
import json
from passlib.hash import bcrypt

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class UsersDB:

    def __init__(self):
        self.connection = sqlite3.connect("users.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return

    def __del__(self):
        self.connection.close()
        return

    def getUsers(self):
    	self.cursor.execute("SELECT * FROM users")
    	return self.cursor.fetchall()

    def getUser(self, email):
    	self.cursor.execute("SELECT * FROM users WHERE email = (?)", (email,))
    	return self.cursor.fetchone()

    def getUserId(self, email):
    	self.cursor.execute("SELECT id FROM users WHERE email = (?)", (email,))
    	return self.cursor.fetchone()

    def createUser(self, first_name, last_name, email, password):
        self.cursor.execute("INSERT INTO users (f_name, l_name, email, encrypted_password) VALUES (?, ?, ?, ?)", (first_name, last_name, email, password))
        self.connection.commit()
        return

def main():
    db = UsersDB()
    db.createUser(name,phone,ethnicity,she_from, body_type, does)
    rows = db.getUsers()
    print(json.dumps(rows))

if __name__ == "__main__":
	main()
