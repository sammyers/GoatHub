from flask import render_template , request, redirect
from app import app
from operator import itemgetter
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


    sorteddict = sorted(goats.items(), key=lambda e: e[1][1],reverse = True)

    top10 = []
    ordered = []
    votes = []

    w = 0
    while w<=9:
        top10.append(sorteddict[w][1])
        w += 1

    x = 0
    while x<=9:
        ordered.append(top10[x][0])
        x += 1

    y = 0
    while y<=9:
        votes.append(top10[y][1])
        y += 1

    
    goatrank1 = ordered[0]
    goatrank2 = ordered[1]
    goatrank3 = ordered[2]
    goatrank4 = ordered[3]
    goatrank5 = ordered[4]
    goatrank6 = ordered[5]
    goatrank7 = ordered[6]
    goatrank8 = ordered[7]
    goatrank9 = ordered[8]
    goatrank10 = ordered[9]

    upgoats1 = votes[0]
    upgoats2 = votes[1]
    upgoats3 = votes[2]
    upgoats4 = votes[3]
    upgoats5 = votes[4]
    upgoats6 = votes[5]
    upgoats7 = votes[6]
    upgoats8 = votes[7]
    upgoats9 = votes[8]
    upgoats10 = votes[9]

    return render_template('rankings.html',
                            goatrank1=goatrank1,
                            upgoats1=upgoats1,
                            goatrank2=goatrank2,
                            upgoats2=upgoats2,
                            goatrank3=goatrank3,
                            upgoats3=upgoats3,
                            goatrank4=goatrank4,
                            upgoats4=upgoats4,
                            goatrank5=goatrank5,
                            upgoats5=upgoats5,
                            goatrank6=goatrank6,
                            upgoats6=upgoats6,
                            goatrank7=goatrank7,
                            upgoats7=upgoats7,
                            goatrank8=goatrank8,
                            upgoats8=upgoats8,
                            goatrank9=goatrank9,
                            upgoats9=upgoats9,
                            goatrank10=goatrank10,
                            upgoats10=upgoats10)


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
