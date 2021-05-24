from app import app
from flask import render_template
from datetime import datetime

user_details = {"username": "ByteSize", "website": "https://bytesize.codes"}

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user=user_details, motto="Make links shrink", site_name="ByteSize Link Shrinker", time=datetime.now())

@app.route('/user')
def user():
    return render_template("user.html", user=user_details, motto="Make links shrink", site_name="ByteSize Link Shrinker")

@app.route('/<path:link>')
def shortened_link(link):
	link_details = {"href": "https://twitter.com/ByteSizeEvents", "endpoint": link}
	return render_template("link.html", link_details=link_details, motto="Make links shrink", site_name="ByteSize Link Shrinker")
