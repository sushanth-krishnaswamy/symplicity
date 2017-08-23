from flask import Flask, render_template, request
from operator import itemgetter

import os
app = Flask(__name__)
 
poll_data = {
   'question' : 'Which is your favourite fruit Sam?',
   'fields'   : ['Apple', 'Orange', 'Banana', 'Pineapple']
}
filename = 'data.txt'
 
@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)
 
@app.route('/poll')
def poll():
    vote = request.args.get('field')
 
    out = open(filename, 'a')
    out.write( vote + '\n' )
    out.close()
 
    return render_template('thankyou.html', data=poll_data)
 
@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0
 
    f  = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1
    votes_sorted = sorted(votes.items(), key=itemgetter(1), reverse = True)
    return render_template('results.html', data=poll_data, votes=votes)
 
 
 
if __name__ == "__main__":
    app.run(debug=True)