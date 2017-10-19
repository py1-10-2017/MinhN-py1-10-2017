import mySQLConnection
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "my secret sesssssion keey"

connection = mySQLConnection.MySQLConnector(app, "facebook")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add_user', methods=["POST"])
def add():
	data = {
		"one":request.form["first_name"],
		"two":request.form["last_name"],
		"three":request.form["email"],
		"four":request.form["dob"]
	}
	query = "INSERT INTO users (`first_name`, `dob`, `last_name`, `email`) VALUES (:one, :four, :two, :three)"
	print request.form
	connection.query_db(query, data)
	return "got ma data"

@app.route('/users')
def users():
	all_users = connection.query_db("SELECT * FROM users ORDER BY first_name")
	all_posts = connection.query_db("SELECT * FROM posts JOIN users ON users.id = posts.user_id")
	print all_posts
	# print all_users
	return render_template('users.html', users=all_users, posts=all_posts)
app.run(debug=True)