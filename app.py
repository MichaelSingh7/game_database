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


@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId('review_id')},
                   {
                     'review_name': request.form.get('review_name'),
                     'genre_name': request.form.get('genre_name'),
                     'review_content': request.form.get('review_content'),
                     'review_date': request.form.get('review_date'),
                     'is_urgent': request.form.get('is_urgent')
    })
    return redirect(url_for('get_reviews'))


@app.route('/delete_review/<review_id>') 
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    return redirect(url_for('get_reviews'))


@app.route('/get_genre')
def get_genre():
    return render_template('genre.html',
                           genre=mongo.db.genre.find())


@app.route('/edit_genre/<genre_id>')
def edit_genre(genre_id):
    return render_template('editgenre.html',
                           genre=mongo.db.genre.find_one(
                                {'_id': ObjectId(genre_id)}))


@app.route('/update_genre/<genre_id>', methods=['POST'])
def update_genre(genre_id):
    mongo.db.genre.update(
        {'_id': ObjectId(genre_id)},
        {'game_genre': request.form.get('game_genre')})
    return redirect(url_for('get_genre'))  


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
