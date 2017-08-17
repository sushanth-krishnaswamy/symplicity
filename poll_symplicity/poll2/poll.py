from flask import Flask, render_template
import os
app = Flask(__name__)
 
poll_data = {
   'question' : 'Which is your favourite fruit?',
   'fields'   : ['Apple', 'Orange', 'Banana', 'Pineapple']
}
 
@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)
 
if __name__ == "__main__":
    app.run(debug=True)