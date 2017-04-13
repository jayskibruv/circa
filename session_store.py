#dictionary of dictionaries
#key = session id (has to be unique): {"user id" (primary key in database): "bleh", "swag": "none"}
import base64, os

class SessionStore:

    def __init__ (self):
        self.sessionData = {}
        return

    def createSession(self):
        sessionId = self.generateSessionId()
        self.sessionData[sessionId] = {}
        return sessionId

    def getSession(self, sessionId):
        if sessionId in self.sessionData:
            return self.sessionData[sessionId]
        else:
            return None

    def generateSessionId(self):
        rnum = os.urandom(32)
        rstr = base64.b64encode(rnum).decode("utf-8")
        return rstr
