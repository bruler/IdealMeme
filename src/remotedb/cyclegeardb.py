#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function


__author__ = "Kapil Gupta"
__copyright__ = "Copyright 2016, TheMallCloud"
__credits__ = ["Kapil Gupta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Kapil Gupta"
__email__ = "kpgupta98@gmail.com"
__status__ = "Production"

import psycopg2
import pprint
import csv
import sys
import os.path

sys.path.append('..')
path_to_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data",  "cyclegear.csv")

connection_str = "dbname='cyclegear' port='5439' user='admin' password='Pragmas0ft' \
 host='mall-cloud-analyzer.cyaf02s2fx7z.us-east-1.redshift.amazonaws.com'"
print('[#] Connecting to \n        -> %s' %connection_str)

conn = psycopg2.connect(connection_str)

column_names = []
rows = 0

cur = conn.cursor()
cur.execute("select top 1000 * from cyclegeartransaction")
rows = cur.fetchall()
all_rows = [row for row in rows]

print(all_rows[0])

with open(path_to_csv, 'w') as f :
    writer = csv.writer(f, delimiter=',')
    column_names = [val[0] for val in cur.description]
    writer.writerow(column_names)  
    for row in all_rows :
        writer.writerow(row)

print('[#] Data Copied')

conn.commit()
conn.close()
