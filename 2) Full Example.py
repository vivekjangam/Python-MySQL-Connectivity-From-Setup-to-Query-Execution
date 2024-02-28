import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",                # please rightly mention user Name from your database here instead of "yourusername" eg:"root"
    password="yourpassword",            # please rightly mention user Name from your database here instead of "yourpassword"
    database="yourdatabase"             # please rightly mention user Name from your database here instead of "yourdatabase"
)

print("Connected to MySQL database!")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute SQL query
mycursor.execute("SELECT * FROM yourtable")   # please rightly mention table Name from your database here

# Fetch the result
result = mycursor.fetchall()

# Print the result
for row in result:
    print(row)

# Close the connection
mydb.close()
print("Connection closed.")

# This is a basic example of MySQL connectivity in Python.
# You can extend it to perform more complex operations such as inserting, updating, or deleting data, as well as handling errors and exceptions