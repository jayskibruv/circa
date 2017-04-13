# A U T H E N T I C A T I O N #

#1. receive e-mail + password
#2. find user by email
  #a. not found: FAIL (either e-mail or password doesn't work)
  #b. found:
    #i. validate password


#validate password:
 #1. verify/compare using provided password with hash from DB
 #
 #
 # plain_password = raw_input("Give me a password: ")
 # hashed_password = bcrypt.hash(plain_password)
 #
 # print("Your hashed password: ")
 # print(hashed_password)
 #
 # password_again = raw_input("Give me your password again: ")
 #
 # if bcrypt.verify(password_again, hashed_password):
 #     print("Matched!")
 # else:
 #     print("Fail. Bye Felicia.")
    #a. didn't match: FAIL
    #b. did match: SUCCESS
        #i. remember user: save their user ID into session store

#POST /sessions

#success
#Status 201

#failure
#Status 401

#cookie
#the one the client sends to the server

#set cookie
#assign browser a new value
