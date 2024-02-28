'''    *CRUD operations for your project by using function*
CRUD operations refer to Create, Read, Update, and Delete operations, which are commonly performed on data in a database. In Python, you can perform CRUD operations using MySQL by connecting to the database and executing SQL queries. Here's how you can implement CRUD operations using functions in Python with MySQL connectivity:
'''

'''
step:1 - Connect to MySQL Database: First, you need to establish a connection to your MySQL database. You can use the mysql.connector module in Python to achieve this:
'''

import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

'''
step: 2 [insert] - Create Function to Insert Data (Create operation): You can create a function to insert new records into a table:
'''
def insert_data(name, email):
    cursor = mydb.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

'''
step: 3 [read] - Create Function to Retrieve Data (Read operation): You can create a function to retrieve records from a table:
'''
def retrieve_data():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    return result

'''
step: 4 [update] - Create Function to Update Data (Update operation): You can create a function to update existing records in a table:
'''
def update_data(id, new_name):
    cursor = mydb.cursor()
    sql = "UPDATE users SET name = %s WHERE id = %s"
    val = (new_name, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

'''
step: 5 [delete]  - Create Function to Delete Data (Delete operation): You can create a function to delete records from a table:
'''
def delete_data(id):
    cursor = mydb.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

'''
With these functions, you can perform CRUD operations on a MySQL database in Python. Just call the appropriate function with the necessary parameters to execute the corresponding SQL query. Make sure to handle exceptions and close the database connection properly for robust error handling and resource management.
'''


'''                                  Thank You                                  '''