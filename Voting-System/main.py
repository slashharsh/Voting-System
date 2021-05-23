from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import os


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://" + os.environ["DB_PORT_27017_TCP_ADDR"] + ":27017/flask_vote"
# mongo = PyMongo(app, "mongodb://localhost:27017/flask_vote")

# Poll Question and Answers #
poll_data_1 = {
    "question": "Which Langugage do you use for Programming?",
    "fields": ["C/C++", "Python", "Java", "JavaScript", "PHP"]
}

# Rendering First (Landing Page) #


@app.route('/')
def root():
    return render_template('index.html', data=poll_data_1)

# Accepting Votes #


@app.route('/poll')
def poll():
    vote = request.args.get('field')
    output = mongo.db.vote_data.insert_one({'vote': vote})
    return render_template('thankyou.html', data=poll_data_1)

# Display Results #


@app.route('/result')
def result():
    votes = {}
    get_votes = mongo.db.vote_data.aggregate([
        {'$group': {'_id': '$vote', 'count': {'$sum': 1}}}
    ])
    for count in get_votes:
        values = {count['_id']: count['count']}
        votes.update(values)
    return render_template('results.html', data=poll_data_1, votes=votes)


if __name__ == '__main__':
    app.run(debug=True)
