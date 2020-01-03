import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'game_database'
app.config["MONGO_URI"] = 'mongodb+srv://root:t00rUser@myfirstcluster-f87ek.mongodb.net/game_database?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html",
                           reviews=mongo.db.reviews.find())


@app.route('/add_review')
def add_review():
    return render_template('addreview.html',
                           genre=mongo.db.genre.find())


@app.route('/insert_review', methods=['POST'])   
def insert_review():
    review = mongo.db.reviews
    review.insert_one(request.form.to_dict()) 
    return redirect(url_for('get_reviews'))                   


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    _review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    _genre = mongo.db.genre.find()
    genre_list = [genre for genre in _genre]
    return render_template('editreview.html',
                           review=_review, genre=genre_list)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
