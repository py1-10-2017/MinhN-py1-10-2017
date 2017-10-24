from flask import Flask, request, session, render_template, flash, redirect
import myconnection
app = Flask(__name__)
app.secret_key = "my super dooper secret keey"
connection = myconnection.MySQLConnector(app, "friends")


@app.route('/')
def index():
	users = connection.query_db("SELECT * FROM users")
	return render_template('index.html', all_users=users)

@app.route('/users', methods=["POST"])
def add():
	data = {
		"name_of_user":request.form["name_of_user"]
	}
	connection.query_db("INSERT INTO users (`name`) VALUES (:name_of_user);", data)
	return redirect("/")
@app.route('/friendships')
def add_friend_page():
	users = connection.query_db("SELECT * FROM users")
	return render_template("friendship.html", all_users=users)
@app.route('/friendships', methods=["POST"])
def add_friends():
	data = {
		"user_id":request.form["user_id"],
		"friend_id":request.form["friend_id"]
	}
	connection.query_db("INSERT INTO user_has_friends (`user_id`, `friend_id`) VALUES (:user_id, :friend_id);", data)
	return redirect("/friendships")
@app.route('/display_friends/<user_id>')
def users(user_id):
	query = "SELECT * FROM user_has_friends JOIN users ON friend_id = users.id WHERE user_id = " + user_id
	all_friends = connection.query_db(query)
	return render_template('show.html', friends=all_friends)

@app.route('/edit/<user_id>')
def edit(user_id):
	query = "SELECT * FROM users WHERE id = " + user_id
	user = connection.query_db(query)
	print user
	return render_template('edit.html', user=user[0])
@app.route('/edit/<user_id>', methods=["POST"])
def update(user_id):
	data = {
		"name":request.form["name"],
		"user_id":user_id
	}
	query = "UPDATE `friends`.`users` SET `name`=:name WHERE `id`=:user_id;"
	user = connection.query_db(query, data)
	return redirect("/")


app.run(debug=True)