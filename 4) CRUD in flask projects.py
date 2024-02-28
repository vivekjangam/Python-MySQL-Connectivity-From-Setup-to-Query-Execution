'''
To perform CRUD operations in Flask with MySQL connectivity, you'll need to follow these steps:'''

'''
step:1 - Install Required Libraries: Install the necessary libraries using pip:
pip install Flask mysql-connector-python
'''

'''
step:2 - Set Up Flask App: Create a Flask application (app.py) and set up MySQL connectivity:
'''
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

'''
    We import necessary modules: Flask for creating the web application, render_template for rendering HTML templates, request for accessing form data, redirect and url_for for redirecting requests, and mysql.connector for MySQL database connectivity.
'''

'''
step:3 - Flask App Configuration: We create a Flask application instance
'''
app = Flask(__name__)

'''
step:4 - MySQL Connection Configuration: 
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

'''
        We establish a connection to the MySQL database. Replace "localhost", "username", "password", and "mydatabase" with your actual MySQL server details.
'''

'''
step:5 - Route for Index Page: 
'''
@app.route('/')
def index():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template('index.html', users=users)

''' 
      When a user visits the root URL (`/`), this route function is executed.
      We create a cursor object to execute SQL queries.
      We execute a 'SELECT' query to fetch all records from the users table.
      We fetch the result using 'fetchall()' and pass it to the 'index.html' template for rendering.
'''

'''
step: 6 - Create HTML Template: Create an HTML template ('index.html') to display user data and provide forms for CRUD operations:  This HTML template displays a list of users and a form to add a new user.
It uses Jinja templating to iterate over the users list passed from the Flask route
'''
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Operations</title>
</head>
<body>
    <h1>Users</h1>
    <ul>
        {% for user in users %}
        <li>{{ user.id }} - {{ user.name }} - {{ user.email }}</li>
        {% endfor %}
    </ul>
    <h2>Add User</h2>
    <form action="/add_user" method="post">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Add User</button>
    </form>
</body>
</html>

kindly uncomment this html code for your use
'''

'''
step: 7 - Route for Adding User: 
'''
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    mydb.commit()
    cursor.close()
    return redirect(url_for('index'))

# Similarly, define routes for update, delete, and other CRUD operations 

'''
      When the form in index.html is submitted, this route function is executed.
      We extract the name and email values from the form data.
      We execute an INSERT query to add a new user to the users table.
      We commit the transaction and close the cursor.
      Finally, we redirect the user back to the index page to see the updated list of users.
'''

'''
step: 8 - Run the Flask App:  This conditional block ensures that the Flask app is only run when the script is executed directly, not when it's imported as a module. It also enables debug mode for development.'''
if __name__ == '__main__':
    app.run(debug=True)


'''
This is a basic example of how to perform CRUD operations with Flask and MySQL connectivity. You can further expand it by adding routes for update, delete, and other CRUD operations as needed. Additionally, make sure to handle exceptions and close database connections properly for better error handling and resource management.
'''


'''                 Thank You                 '''