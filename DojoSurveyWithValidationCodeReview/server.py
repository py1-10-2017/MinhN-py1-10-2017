from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "ryans secret key"

@app.route('/')
def index():
	if "data" in session.keys():
		name = session["data"]["name"]
		location = session["data"]["location"]
		language = session["data"]["language"]
		comment = session["data"]["comment"]
		return render_template("index.html", name=name, location=location, language=language, comment=comment)
	else:
		return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	valid = True
	if name == "":
		valid = False
		flash("name is empty")
	if comment == "":
		valid = False
		flash("comment is empty")
	elif len(comment) > 120:
		valid = False
		flash("comment is longer than 120")
	if valid == True: #true
		session["data"] = {
			"name" : request.form['name'],
			"location" : request.form['location'],
			"language" : request.form['language'],
			"comment": request.form["comment"]
		}
		return redirect('/display')
	if valid == False:
		session["data"] = {
			"name" : request.form['name'],
			"location" : request.form['location'],
			"language" : request.form['language'],
			"comment" : request.form['comment']
		}
		return redirect('/')

@app.route('/display')
def display():
	if "data" in session.keys():
		name = session["data"]["name"]
		location = session["data"]["location"]
		language = session["data"]["language"]
		commend = session["data"]["commend"]
	return render_template("submit.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True)
# Also, validate that the comment field is no longer than 120 characters.

#1. all validations pass-> redirect to display
#2. not all validations pass-> redirect to the form w/ errors