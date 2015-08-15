#!/usr/bin/python

# https://gist.github.com/bertspaan/8220892

import csv
from dbfpy import dbf
import os
import sys

filename = sys.argv[1]
if filename.endswith('.dbf'):
  print "Converting %s to csv" % filename
  csv_fn = filename[:-4]+ ".csv"
  with open(csv_fn,'wb') as csvfile:
    in_db = dbf.Dbf(filename)
    out_csv = csv.writer(csvfile)

    cols = {}
    names = []
    for field in in_db.header.fields:
      field_name = field.name.lower()
      cols[field_name] = cols[field_name] + 1 if field_name in cols else 1
      if cols[field_name] > 1:
        field_name += str(cols[field_name])
      names.append(field_name)
    out_csv.writerow(names)

    for rec in in_db:
      out_csv.writerow(rec.fieldData)
    in_db.close()
    print "Done..."
else:
  print "Filename does not end with .dbf"
