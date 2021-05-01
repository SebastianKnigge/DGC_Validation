import sqlite3

connection = sqlite3.connect(':memory:')
# Currently running in the local memory, otherwise uncomment the next line
# connection = sqlite3.connect('userDB.db')

#Creating the cursor for database operations
c = connection.cursor()

# Creating the database
c.execute("""CREATE TABLE userDB(
    id integer PRIMARY KEY UNIQUE,
    firstname text,
    lastname text,
    company text,
    mail text UNIQUE,
    password text,
    api_call_counter integer
)""")
connection.commit()

# Creating the user
c.execute("INSERT INTO userDB VALUES(1,'Sebastian','Knigge','Team', 'sebastian-knigge@live.de', 'abcd', 0)")
c.execute("INSERT INTO userDB VALUES(2,'Felix','Biler','Team', 'fbxx@live.de', 'efgh', 0)")
connection.commit()

# The function to verify the users APIkey/password
def verifier(verify):
    result = False
    c.execute("SELECT * FROM userDB WHERE password=?", (verify,))
    SQL_result = c.fetchone()
    if SQL_result != None:
        result = True
    return result, SQL_result[0], SQL_result[1], SQL_result[2], SQL_result[3]

