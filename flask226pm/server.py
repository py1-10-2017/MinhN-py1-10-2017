from flask import Flask, render_template, session, redirect, request
from myconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
app.secret_key = "asdjflasjdfla;sdf"

# an example of running a query
users = mysql.query_db("SELECT * FROM users")

[
	{"last_name":"Hart", "first_name":"Beth", "DOB":"2017-01-01"},
	{"last_name":"Danny", "first_name":"Hua", "DOB":"2017-01-01"}
]
print users
import random
@app.route('/')
def index():
	if not "correct_number" in session.keys(): # array of keys
		session["correct_number"] = random.randrange(0, 101)
	if "current_state" in session.keys():
		return render_template("display.html")
	else:
		return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
	print request.form["guess"]
	print session["correct_number"]
	if int(request.form["guess"]) == session["correct_number"]:
		session["current_state"] = "correct!"
	elif int(request.form["guess"]) > session["correct_number"]:
		session["current_state"] = "to high"
	else:
		session["current_state"] = "to low"
	return redirect('/')


app.run(debug=True)

# do i need to initiate a session variable/check for key
# what do i need to store in order to use in my redirect