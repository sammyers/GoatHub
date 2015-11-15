from flask import render_template , request, redirect
from app import app
import random
import csv
goats = {}
leftgoat = 1
with open('goats.csv','r') as csvfile:
    goatscsv = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in goatscsv:
        goatvalue = int(row[0])
        goaturl = row[1]
        goatrank = int(row[2])
        goats[goatvalue]= [goaturl,goatrank]

@app.route('/')

@app.route('/index')

def index():
    global goats
    goatid1 = random.randrange(1,len(goats)+1,1)
    goatid2 = random.randrange(1,len(goats)+1,1)
    # main page
    goatdic1 = goats[goatid1]
    goatdic2= goats[goatid2]
    goaturl1 = goatdic1[0]
    goaturl2= goatdic2[0]
    return render_template('index.html',
                           goatid1 = goatid1,
                           goatid2 = goatid2,
                           goaturl1 = goaturl1,
                           goaturl2 = goaturl2,
                        
                           )
    
@app.route('/rankings')
def rankings():
    #Rankings page
    global goats
    
    
    return render_template('rankings.html',
                            goatrank1 = goatrank1
                            goatrank2 = goatrank2
                            goatrank3 = goatrank3
                            goatrank4 = goatrank4
                            goatrank5 = goatrank5
                            goatrank6 = goatrank6
                            goatrank7 = goatrank7
                            goatrank8 = goatrank8
                            goatrank9 = goatrank9
                            goatrank10 = goatrank10)

@app.route('/about')
def about():
    #about us page
    return render_template('about.html')

@app.route('/goatvote',methods = ['POST'])
def goatvote():
   
    #executes on vote . Name of goat buttons are goatbutton, 
    goatid = int(request.form['goatbutton'])
    goatentry = goats[goatid]
    goatentry[1] += 1
    goats[goatid] = goatentry
        
    
    
    return redirect('/')
