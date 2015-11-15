from flask import render_template , request, redirect
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

print ordered

y = 0
while y<=9:
    votes.append(top10[y][1])
    y += 1

print votes