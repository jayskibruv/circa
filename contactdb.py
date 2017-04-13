import sqlite3 #eventually replace with psyco
# import random
import json
#import psycopg2
#import psycopg2.extras

#ditch later
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class ContactsDB:

	def __init__(self):
		self.connection = sqlite3.connect("contacts.db")
		self.connection.row_factory = dict_factory
		self.cursor = self.connection.cursor()
		return

	def __del__(self):
		self.connection.close()
		return

	def getContacts(self):
		self.cursor.execute("SELECT * FROM contacts")
		return self.cursor.fetchall()

	def createContacts(self, name, phone, ethnicity, she_from, body_type, does):
		self.cursor.execute("INSERT INTO contacts (name, phone, ethnicity, she_from, body_type, does) VALUES (?, ?, ?, ?, ?, ?)", (name, phone, ethnicity, she_from, body_type, does))
		self.connection.commit()
		return

	def deleteContact(self,shawty_id):
		self.cursor.execute("DELETE FROM contacts WHERE id = (?)", (shawty_id,))
		self.connection.commit()
		return

	def getContact(self, shawty_id):
		self.cursor.execute("SELECT * FROM contacts WHERE id = (?)", (shawty_id,))
		return self.cursor.fetchone()

	def editContact(self,shawty_id, name, phone, ethnicity, she_from, body_type, does):
		self.cursor.execute("UPDATE contacts SET name = (?), phone = (?), ethnicity = (?), she_from = (?), body_type = (?), does = (?) WHERE id = (?)", (name, phone, ethnicity, she_from, body_type, does,shawty_id))
		self.connection.commit()
		return



def main():
	db = ContactsDB()
	db.createContacts(name,phone,ethnicity,she_from, body_type, does)
	rows = db.getContacts()
	print(json.dumps(rows))

if __name__ == "__main__":
	main()
