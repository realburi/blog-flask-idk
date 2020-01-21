from flask import Flask, render_template, request, url_for 

web = Flask(__name__)

@web.route("/")
def index():
	return render_template("index.html")

@web.route("/about")
def about():
	return render_template('about.html')

@web.route("/contact")
def contact():
	return render_template("contact.html")

@web.route("/post")
def post():
	return render_template("post.html")
		
web.run(host="0.0.0.0", port=5000, debug=True)
