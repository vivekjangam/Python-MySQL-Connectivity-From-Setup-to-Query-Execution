'''  LEARN Python MySQL Connectivity in JUST 4 STEPS.... 
To establish MySQL connectivity in Python, you can use the mysql-connector-python library, which provides a Python interface for MySQL databases. Below is a step-by-step guide along with code examples to demonstrate how to connect to a MySQL database from Python:
'''


'''
Step 1: Install MySQL Connector Python
You need to install the mysql-connector-python library. You can install it via pip:

--->  pip install mysql-connector-python   (You can Just copy paste it to your code terminal)
'''

'''
Step 2: Connect to MySQL Database
'''
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

print("Connected to MySQL database!")

# Replace "localhost", "yourusername", "yourpassword", and "yourdatabase" with your MySQL server details.




'''
Step 3: Execute SQL Queries
You can now execute SQL queries using the connection object mydb. Here's an example of executing a simple query to fetch data:
'''
# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute SQL query
mycursor.execute("SELECT * FROM yourtable")

# Fetch the result
result = mycursor.fetchall()

# Print the result
for row in result:
    print(row)


# Replace "yourtable" with the name of your table.

'''
Step 4: Close the Connection
After you are done with database operations, don't forget to close the connection:
'''
# Close the connection
mydb.close()
print("Connection closed.")