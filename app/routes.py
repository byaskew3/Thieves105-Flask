from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    instructors = [{
        'name': 'Christian',
        'age': 9000
    },
    {
        'name': 'Christopher',
        'age': 'infinity'
    }]
    return render_template('index.html', names=instructors)