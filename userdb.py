import os
import psycopg2
import psycopg2.extras
import urllib.parse
import json
from passlib.hash import bcrypt

class UsersDB:

    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

        self.connection = psycopg2.connect(
            cursor_factory=psycopg2.extras.RealDictCursor,
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        return

    def getUsers(self):
    	self.cursor.execute("SELECT * FROM users")
    	return self.cursor.fetchall()

    def getUser(self, email):
    	self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    	return self.cursor.fetchone()

    def getUserId(self, email):
    	self.cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    	return self.cursor.fetchone()

    def createUsersTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, f_name, l_name, email, encrypted_password)")
        self.connection.commit()

    def createUser(self, first_name, last_name, email, password):
        self.cursor.execute("INSERT INTO users (f_name, l_name, email, encrypted_password) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, password))
        self.connection.commit()
        return

def main():
    db = UsersDB()
    db.createUser(name,phone,ethnicity,she_from, body_type, does)
    rows = db.getUsers()
    print(json.dumps(rows))

if __name__ == "__main__":
	main()
