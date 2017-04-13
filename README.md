
### Name of Resources:



>* **users.db**
>* **contacts.db**

----------

### 'users.db' Resource Attributes:




>* id
* first name
* last name
* email
* password

----------
### 'contacts.db' Resource Attributes:

>* id
* name
* phone
* ethnicity
* she_from
* body_type
* does
  * think: occupation.

----------

### 'users.db' Table Schema:


    CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    fname VARCHAR,
    lname VARCHAR,
    email VARCHAR,
    password VARCHAR );


----------
### 'contacts.db' Table Schema:


    CREATE TABLE contacts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone INTEGER NOT NULL,
    ethnicity TEXT NULL,
    she_from TEXT NULL,
    body_type TEXT NULL,
    does TEXT NULL );


----------


### REST API:


>* GET | /users | handleUserList()
  * **Retrieves *all* users** (not really practical for this assignment)
* POST | /users | handleUserCreate()
  * **Response for registering a user**
* POST | /sessions | handleUserAuthentication()
  *  **Creates session upon user authentication**
* GET | /contacts | handleResource()
  * **Retrieves data from 'contacts.db'**

----------

### Hashing:

>The hashing method used to encrypt password data is the bcrypt function.