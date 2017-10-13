from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "sometihng secret"

@app.route('/', methods=["GET"])
def index():
	if 'first_name' in session.keys():
		name = session["first_name"]
		print name
		return render_template("index.html", context={"x":name, "last":session["last_name"]})
	return "no name"

@app.route('/login', methods=["GET"])
def login():
	return render_template('form.html')

@app.route('/process_login', methods=["POST"])
def process_login():
	session["first_name"] = request.form["first_name"]
	session["last_name"] = request.form["last_name"]

	return redirect('/')

@app.route('/clear_session')
def clear():
	session.clear()
	return redirect('/')
app.run(debug=True)