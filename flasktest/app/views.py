from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    # main page
    return render_template('index.html',
                           title='Home')
@app.route('/about')
def rankings():
    #Rankings page
    return render_template('about.html',
                           title ='Home')

@app.route('/about')
def about():
    #about us page
    return render_template('about.html',
                           title ='Home')
