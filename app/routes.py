from app import app, database
from flask import render_template, redirect, url_for, request
from datetime import datetime

user_details = {"username": "ByteSize", "website": "https://bytesize.codes"}

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user=user_details, motto="Make links shrink", site_name="ByteSize Link Shrinker", time=datetime.now())

@app.route('/user')
def user():
    return render_template("user.html", user=user_details, motto="Make links shrink", site_name="ByteSize Link Shrinker")

@app.route('/user/create', methods=['GET', 'POST'])
def user_create():
	if request.method == 'GET':
	    return render_template("user_create.html", user=user_details, motto="Make links shrink", site_name="ByteSize Link Shrinker")
	elif request.method == 'POST':
		link_name = request.form["link_name"]
		link_href = request.form["link_href"]
		shorturl = database.create_link(str(link_name), str(link_href))
		return redirect(url_for("user_create_submit", link = shorturl))

@app.route('/user/created/<string:link>', methods=['GET'])
def user_create_submit(link):
	print(f"Link requested is '{link}'")
	link_details = database.fetch_link(str(link))
	return render_template("user_created.html", link_details=link_details, user=user_details, motto="Make links shrink", site_name="ByteSize Link Shrinker")

@app.route('/<string:link>')
def shortened_link(link):
	print(f"Link requested is '{link}'")
	link_details = database.fetch_link(str(link))
	return render_template("link.html", link_details=link_details, motto="Make links shrink", site_name="ByteSize Link Shrinker")
