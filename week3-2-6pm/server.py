from flask import Flask, request, session, render_template, flash, redirect
import myconnection
app = Flask(__name__)
app.secret_key = "my super dooper secret keey"
connection = myconnection.MySQLConnector(app, "mydb")
# print connection.query_db("INSERT INTO users (`first_name`, `last_name`, `DOB`) VALUES ('Nort', 'Mahoney', '2017-04-01');")
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/add_to_db', methods=["POST"])
def add():
	#injected "minh', 'last_name', '2017-04-01'); SET foreign_key_checks = 0; DROP TABLE users;" works
	query = "INSERT INTO users (`first_name`, `last_name`, `DOB`) VALUES ('{}', '{}', '{}');".format(request.form["first_name"], request.form["last_name"], request.form["dob"])

	num_users = connection.query_db(query)
	print num_users
	return  query
	return "Got {} users".format(num_users)

@app.route('/users')
def users():
	query = "SELECT * FROM users"
	all_users = connection.query_db(query)
	return render_template('users.html', users=all_users)

app.run(debug=True)