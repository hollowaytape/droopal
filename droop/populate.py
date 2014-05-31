import os
import csv
import sqlite3
import datetime

conn = sqlite3.connect('droop.db')
c = conn.cursor()

with open(data, 'rb') as f:
    plotlist = csv.reader(f, delimiter=',')
    plotlist.next()
    plotlist.next()
    for i, line in enumerate(plotlist):
        id = i
        