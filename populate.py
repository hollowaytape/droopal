import os
import csv
import sqlite3
import datetime

data = "fakedata.csv"
conn = sqlite3.connect('droop.db')
c = conn.cursor()

with open(data, 'rb') as f:
    plotlist = csv.reader(f, delimiter=',')
    plotlist.next()
    plotlist.next()
    for i, line in enumerate(plotlist):
        id = int(line[0])
        # Next: Name could be Type/Number/NearestStreet with a reverse geocoding API.
        name = "Apple %s" % (id)
        type = "Apple"
        threshold = int(line[1])
        ripeness = int(line[2])
        lat = float(line[3])
        long = float(line[4])
        
        date_time = datetime.datetime.strptime(line[5], "%m/%d/%y").date()
        value = int(line[6])
        
        tree = (id, name, type, threshold, ripeness, lat, long)
        reading = (i, id, date_time, value)
        
                    
        sql_a = "INSERT INTO droop_tree (id, name, type, threshold, ripeness, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
        sql_b = "INSERT INTO droop_reading (id, tree_id, date_time, value) VALUES (?, ?, ?, ?)"
        
        c.execute(sql_b, reading)
        
        try:
            c.execute(sql_a, tree)
        except sqlite3.IntegrityError:
            continue
            
conn.commit()
conn.close()