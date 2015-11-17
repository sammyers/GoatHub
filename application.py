#!/usr/bin/env python

from flask import Flask, render_template, request, redirect
from application import db
from application.models import Goat
from application.forms import EnterDBInfo, RetrieveDBInfo
import random
import csv

from flask.ext.sqlalchemy import SQLAlchemy

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
application.secret_key = 'c6qNFknUx3zp8BXSCf16P++rzGMu+L8SmjPMJE1c3'


@application.route('/')
@application.route('/index')
def index():
    goats = Goat.query.all()

    left_goat_id = random.randrange(0,len(goats),1)
    right_goat_id = random.randrange(0,len(goats),1)

    while left_goat_id == right_goat_id:
        right_goat_id = random.randrange(0,len(goats),1)

    left_goat = goats[left_goat_id]
    right_goat = goats[right_goat_id]

    return render_template('index.html',
                           left_goat = left_goat,
                           right_goat = right_goat,
                           )

@application.route('/rankings')
def rankings():
    #Rankings page
    goat_query = db.session.query(Goat).order_by(Goat.votes.desc()).limit(10)

    top10 = goat_query

    return render_template('rankings.html',
                            top10 = top10,
                            )

@application.route('/about')
def about():
    #about us page
    return render_template('about.html')

@application.route('/goatvote', methods = ['POST'])
def goatvote():
    #executes on vote . Name of goat buttons are goatbutton 
    goat_id = int(request.form['goatbutton'])

    voted_goat = Goat.query.get(goat_id)

    voted_goat.votes += 1

    db.session.commit()
        
    return redirect('/')

if __name__ == '__main__':
    application.run(host='0.0.0.0')