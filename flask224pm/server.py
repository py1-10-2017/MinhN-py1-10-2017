from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "secret stuff"
import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range


@app.route('/')
def index():
	if not "random_number" in session.keys():
		session["random_number"] = random.randrange(0, 101)
	if "current_answer" in session.keys():
		return render_template("guess.html")
	else:
		return render_template("index.html")
@app.route('/process', methods=["POST"])
def process():
	#process their guess
	print session["random_number"]
	if int(request.form["guess"]) > session["random_number"]:
		session["current_answer"] = "high"
	elif int(request.form["guess"]) < session["random_number"]:
		session["current_answer"] = "low"
	else:
		session["current_answer"] = "correct"
	return redirect('/')

app.run(debug=True)
# person = {
# 	"name":"stephanie"
# }

# console.log(person.last_name) #undefined