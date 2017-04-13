#10

import os
import psycopg2
import psycopg2.extras
import urllib.parse
import json

class ContactsDB:

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

	def getContacts(self):
		self.cursor.execute("SELECT * FROM contacts")
		return self.cursor.fetchall()

    def createContactsTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id SERIAL PRIMARY KEY, phone VARCHAR(255), ethnicity VARCHAR(255), she_from VARCHAR(255), body_type VARCHAR(255), does VARCHAR(255))")
        self.connection.commit()

	def createContacts(self, name, phone, ethnicity, she_from, body_type, does):
		self.cursor.execute("INSERT INTO contacts (name, phone, ethnicity, she_from, body_type, does) VALUES (%s, %s, %s, %s, %s, %s)", (name, phone, ethnicity, she_from, body_type, does))
		self.connection.commit()
		return

	def deleteContact(self,shawty_id):
		self.cursor.execute("DELETE FROM contacts WHERE id = (%s)", (shawty_id,))
		self.connection.commit()
		return

	def getContact(self, shawty_id):
		self.cursor.execute("SELECT * FROM contacts WHERE id = (%s)", (shawty_id,))
		return self.cursor.fetchone()

	def editContact(self,shawty_id, name, phone, ethnicity, she_from, body_type, does):
		self.cursor.execute("UPDATE contacts SET name = (%s), phone = (%s), ethnicity = (%s), she_from = (%s), body_type = (%s), does = (%s) WHERE id = (%s)", (name, phone, ethnicity, she_from, body_type, does,shawty_id))
		self.connection.commit()
		return



def main():
	db = ContactsDB()
	rows = db.getContacts()
	print(json.dumps(rows))

if __name__ == "__main__":
	main()
