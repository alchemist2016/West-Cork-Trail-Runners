import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'treck_running'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/get_trails')
def get_trails():
    return render_template("get_trail.html",
                           trails=mongo.db.trail_running.find())


@app.route('/add_trail')
def add_trail():
    return render_template('addtrail.html',
                           trails=mongo.db.trail_running.find())


@app.route('/insert_trail', methods=['POST'])
def insert_trail():
    trails = mongo.db.trail_running
    trails.insert_one(request.form.to_dict())
    return redirect(url_for('get_trails'))


@app.route('/edit_trail/<trail_id>')
def edit_trail(trail_id):
    the_trail = mongo.db.trail_running.find_one({"_id": ObjectId(trail_id)})
    all_trails = mongo.db.trail_running.find()
    return render_template('edittrail.html', trail=the_trail, trails=all_trails)


@app.route('/update_trail/<trail_id>', methods=['POST'])
def update_trail(trail_id):
    trail = mongo.db.trail_running.find_one({"_id": ObjectId(trail_id)})
    trails = mongo.db.trail_running
    trails.update({"_id": ObjectId(trail_id)}, request.form.to_dict())
    return redirect(url_for('get_trails'))


@app.route('/delete_trail/<trail_id>')
def delete_trail(trail_id):
    mongo.db.trail_running.remove({'_id': ObjectId(trail_id)})
    return redirect(url_for('get_trails'))


@app.route('/get_members')
def get_members():
    return render_template('get_members.html',
                           members=mongo.db.member.find())


@app.route('/add_members')
def add_members():
    return render_template('add_member.html',
                           members=mongo.db.member.find())


@app.route('/insert_member', methods=['POST'])
def insert_member():
    members = mongo.db.member
    members.insert_one(request.form.to_dict())
    return redirect(url_for('get_members'))


@app.route('/edit_member/<member_id>')
def edit_member(member_id):
    the_member = mongo.db.member.find_one({"_id": ObjectId(member_id)})
    all_members = mongo.db.member.find()
    return render_template('editmember.html', member=the_member, members=all_members)


@app.route('/update_member/<member_id>', methods=['POST'])
def update_member(member_id):
    member = mongo.db.member.find_one({"_id": ObjectId(member_id)})
    members = mongo.db.member
    members.update({"_id": ObjectId(member_id)}, request.form.to_dict())
    return redirect(url_for('get_members'))


@app.route('/delete_member/<member_id>')
def delete_member(member_id):
    mongo.db.member.remove({'_id': ObjectId(member_id)})
    return redirect(url_for('get_members'))


@app.route('/contact')
def contact():
    return render_template('contact.html')
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)