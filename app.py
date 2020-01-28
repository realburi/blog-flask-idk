from flask import Flask, render_template, request, url_for, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv, requests
import os
import sys

web = Flask(__name__)

web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/buri/Desktop/startbootstrap-clean-blog-gh-pages/blog.db'
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(web)

class blog_post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@web.route("/")
def index():
	with open("names.csv", encoding='utf-8') as file:
		posts = [data for data in csv.reader(file)]
	return render_template("index.html", posts=posts)

@web.route("/about")
def about():
	return render_template('about.html')

@web.route("/contact")
def contact():
	return render_template("contact.html")

@web.route("/post")
def post():
	try:
		post_id = request.args.get('id')
		with open('names.csv','r',encoding='utf-8') as file:
			reader = csv.reader(file)
			interestingrows=[row for idx, row in enumerate(reader)][int(post_id)]
		return render_template("post.html",post = interestingrows)
	except:
		return render_template('error.html')
	

@web.route("/add")
def add():
	return render_template('add.html')

@web.route("/add_post", methods=['POST'])
def add_post():
	title = request.form['title']
	subtitle = request.form['subtitle']
	author = request.form['author']
	content = request.form['content']
	
	post = blog_post(title=title, subtitle=subtitle, author=author, content=content, date_posted = datetime.now())
	db.session.add(post)
	db.session.commit()

	return redirect(url_for('index'))

@web.route('/add_blog')
def add_blog():
	return render_template('blog.html')

@web.route('/blog_post',methods=['POST'])
def blog_post():
	data = dict(request.form)
	data.update({"date_added" :  str(datetime.utcnow()).split(" ")[0], "id" : requests.get('http://localhost:5000/check_id').text }) 
	with open('names.csv', 'a', newline='', encoding="utf-8") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(data.values())
	return render_template('success.html')

@web.route('/check_id')
def check_id():
	with open('names.csv', 'r',encoding='utf-8') as file:
		reader = csv.reader(file)
		result = len([data for data in reader])
		return str(result)

@web.route('/data')
def data(): 
	return jsonify(dir(db.Query))

if __name__ == "__main__":		
	web.run(host="0.0.0.0", port=5000, debug=True)
