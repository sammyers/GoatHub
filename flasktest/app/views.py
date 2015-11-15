from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    # main page
    return render_template('index.html',
                           title='Home')
@app.route('/rankings')
def rankings():
    #Rankings page
    return render_template('rankings.html',
                           title ='Home')

@app.route('/about')
def about():
    #about us page
    return render_template('about.html',
                           title ='Home')
