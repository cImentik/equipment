# -*- coding: utf-8 -*-

import sqlite3
import csv

s=[]

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

with open('spravph.csv', newline='') as csvfile:
    sreader = csv.reader(csvfile, delimiter='%')
    for row in sreader:
        c.execute("INSERT INTO t_table VALUES ('%s')" % row[3])
        conn.commit()
        #print(row[3])

conn.close()


# CREATE TABLE t_table
# (
#     name varchar(255) NOT NULL
# )