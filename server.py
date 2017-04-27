from http.server import BaseHTTPRequestHandler, HTTPServer
from http import cookies
from urllib.parse import urlparse, parse_qs
from userdb import UsersDB
from contactdb import ContactsDB
from session_store import SessionStore
import json
import sys
import os
from passlib.hash import bcrypt

gSessionStore = SessionStore()
gUsersDB = UsersDB()

class HelloHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin",  "*")
        self.send_header("Access-Control-Allow-Methods","POST, GET, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers","Accept, Content-Type, Origin")
        self.end_headers()
        return

    def do_POST(self):
        self.load_cookie()
        self.load_session()

        if self.path == "/users":
        	self.handleUserCreate()
        elif self.path == "/sessions":
            self.handleUserAuthentication()
        elif self.path == "/contacts":
            self.handleNewContact()
        else:
        	self.handle404()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin",self.headers["Origin"])
        self.send_header("Access-Control-Allow-Credentials","true")
        self.send_cookie()
        BaseHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        self.load_cookie()
        self.load_session()

        if self.path == "/contacts":
            self.handleResource()
        elif self.path == "/sessions":
            if "user_id" in self.session:
                print("USER ID: ", self.session['user_id'])
                self.send_response(200)
                self.end_headers()

            else:
                self.send_response(401)
                self.end_headers()
        else:
            self.handle404()

    def load_session(self):
        if "sessionId" in self.cookie:
            sessionId = self.cookie["sessionId"].value
            self.session = gSessionStore.getSession(sessionId)
            print("SESSION ID: ", sessionId)
            if self.session == None:
                sessionId = gSessionStore.createSession()
                self.cookie["sessionId"] = sessionId
                self.session = gSessionStore.getSession(sessionId)
                print("SESSION ID: ", sessionId)
        else:
            sessionId = gSessionStore.createSession()
            self.cookie["sessionId"] = sessionId
            self.session = gSessionStore.getSession(sessionId)
            print("SESSION ID: ", sessionId)

    def load_cookie(self):
        if "Cookie" in self.headers:
            self.cookie = cookies.SimpleCookie(self.headers["Cookie"])
        else:
            self.cookie = cookies.SimpleCookie()

    def send_cookie(self):
        for morsel in self.cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())

    #GET ALL USERS
    def handleUserList(self):

        self.send_response(200)
        self.send_header("Content-Type", "application/json")

        db = UsersDB()
        db_users = db.getUsers()
        json_log = json.dumps(db_users)

        print("CONTACTS RETRIEVED: ", json_log)
        self.end_headers()
        self.wfile.write(bytes(json_log, "utf-8"))

        return

    def handleNewContact(self):
		length = self.headers['Content-Length']
		length = int(length)

		body = self.rfile.read(length).decode("utf-8")
		data = parse_qs(body)
		json_log = json.dumps(data)
		self.send_response(201)

		self.send_header("Access-Control-Allow-Origin","*")
		self.send_header("Content-Type", "application/x-www-form-urlencoded")

		name = data['name'][0]
		phone = data['phone'][0]
		ethnicity = data['ethnicity'][0]
		she_from = data['she_from'][0]
		body_type = data['body_type'][0]
		does = data['does'][0]
		db = ContactsDB()

		if name != "" or number != "":
			db.createContacts(name, phone, ethnicity, she_from, body_type, does)
		else:
			print("No name or phone number provided. Contact cannot be created.")


		print("CONTACT CREATED: " + json_log)
		self.end_headers()
		return

    def handleResource(self):

        if "user_id" in self.session:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            db = ContactsDB()
            db_contacts = db.getContacts()
            json_log = json.dumps(db_contacts)

            print("CONTACTS RETRIEVED: ", json_log)
            self.end_headers()
            self.wfile.write(bytes(json_log, "utf-8"))

        else:
            self.handle401()

        return

    #POST
    def handleUserCreate(self):
        length = self.headers['Content-Length']
        length = int(length)

        body = self.rfile.read(length).decode("utf-8")
        data = parse_qs(body)
        json_log = json.dumps(data)

        first_name = data['fname'][0]
        last_name = data['lname'][0]
        email = data['email'][0]
        encrypted_password = bcrypt.hash(data['password'][0])

        db = UsersDB()
        if db.getUser(email):
            self.send_response(401)
            print("E-MAIL ALREADY EXISTS IN DATABASE.")
        else:
            self.send_response(201)
            self.send_header("Content-Type", "application/x-www-form-urlencoded")
            db.createUser(first_name, last_name, email, encrypted_password)
            print("USER CREATED: " + "First name: " + first_name + " | " + "Last name: " + last_name + " | " + "E-mail:" + email)
        self.end_headers()
        return

    #GET USER
    def handleUserAuthentication(self):

        length = self.headers['Content-Length']
        length = int(length)

        body = self.rfile.read(length).decode("utf-8")
        data = parse_qs(body)

        auth_email = data['in-email'][0]
        login_password = data['in-password'][0]

        db = UsersDB()
        db_user = db.getUser(auth_email)

        if db_user:
            json_log = json.dumps(db_user)
            if bcrypt.verify(login_password,db_user['encrypted_password']):
                self.session["user_id"] = db_user["id"]
                self.send_response(201)
                self.end_headers()
                self.wfile.write(bytes(json_log,"utf-8"))
                print("Passwords matched! Authorization granted.")
                return True
            else:
                self.handle401()
                print("Passwords do not match. Authorization denied.")
        else:
            self.handle404()
            print("Sorry, I can't get something that doesn't exist.")

    def handle404(self):
    	self.send_response(404)
    	self.send_header("Content-type", "text/html")
    	self.end_headers()
    	self.wfile.write(bytes("<h1>404: Not Found</h1>","utf-8"))

    def handle401(self):
        self.send_response(401)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>401: Unauthorized</h1>","utf-8"))

def main():

    db = ContactsDB()
    db.createContactsTable()
    db = None
    db = UsersDB()
    db.createUsersTable()
    db = None

    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    listen = ("0.0.0.0", port)
    server = HTTPServer(listen, HelloHandler)

    print("Listening on", "{}:{}".format(*listen))
    server.serve_forever()

main()
