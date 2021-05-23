from flask import Flask, render_template, request
import pymongo
import os


app = Flask(__name__)

# Poll Question and Answers
poll_data_1 = {
    "question": "Which Langugage do you use for Programming?",
    "fields": ["C/C++", "Python", "Java", "JavaScript", "PHP"]
}

# Rendering First (Landing Page)


@app.route('/')
def root():
    return render_template('index.html', data=poll_data_1)

# Accepting Votes


@app.route('/poll')
def poll():
    vote = request.args.get('field')
    output = open("vote", "a")
    output.write(vote+'\n')
    output.close()
    return render_template('thankyou.html', data=poll_data_1)

# Display Results
@app.route('/result')
def result():
    votes = {}
    for f in poll_data_1['fields']:
        votes[f] = 0
    
    f = open("vote","r")
    for line in f:
        vote = line.rstrip('\n')
        votes[vote] += 1
    return render_template('results.html', data=poll_data_1, votes=votes)



if __name__ == '__main__':
    app.run(debug=True)
