#!/usr/bin/env python

from os import listdir, path
from os.path import isfile, join
import sys, csv, psycopg2 as dbapi2

onlyfiles = [f for f in listdir("../csvs") if isfile(join("../csvs", f))]

db = dbapi2.connect(database="viewer_taesp_features", user="fortysix")
cur = db.cursor()
db.set_isolation_level(0)
cur.execute("SET CLIENT_ENCODING TO 'LATIN1';")

for f in onlyfiles:
  table_name = "_".join(f.split(".")[:-1])
  csv_path = path.abspath(join("../csvs", f))
  print table_name, "~", csv_path

  try:
    q = "DROP TABLE {0};".format(table_name)
    print ">", q
    db.set_isolation_level(0)
    cur.execute(q)
  except:
    print "Nowt to drop."

  q = "CREATE TABLE {0} ();".format(table_name)
  print ">", q
  db.set_isolation_level(0)
  cur.execute(q)

  with open(csv_path, "rb") as tidy_csv:
    reader = csv.reader(tidy_csv, delimiter=',')
    row = reader.next()

    for field_name in row:
      q = "ALTER TABLE {0} ADD COLUMN \"{1}\" TEXT;".format(table_name, field_name.lower())
      print ">", q
      db.set_isolation_level(0)
      cur.execute(q)

  q = "COPY {0} FROM '{1}' DELIMITERS ',' CSV HEADER;".format(table_name, csv_path)
  print ">", q
  db.set_isolation_level(0)
  cur.execute(q)
