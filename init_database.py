#!/usr/bin/env python

from application import db
from application.models import Goat

import csv

with open('goats.csv','r') as csvfile:
    goatscsv = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in goatscsv:
        goat_url = row[0]
        goat_rank = int(row[1])
        db.session.add(Goat(goat_url, goat_rank))
    db.session.commit()
