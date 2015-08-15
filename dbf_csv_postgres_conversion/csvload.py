#!/usr/bin/env python

from os import listdir, path
from os.path import isfile, join
import sys, csv, psycopg2 as dbapi2

onlyfiles = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f)) and f.endswith('.csv')]

db = dbapi2.connect(database="viewer_taesp", user="viewers")
cur = db.cursor()
db.set_isolation_level(0)
cur.execute("SET CLIENT_ENCODING TO 'LATIN1';")

for f in onlyfiles:
  table_name = "_".join(f.split(".")[:-1])
  table_name = "_".join(table_name.split(" "))
  table_name = "_".join(table_name.split("-"))
  csv_path = path.abspath(join(sys.argv[1], f))
  print table_name, "~", csv_path
  table_name = table_name.lower()

  # @TODO: Need consistent approach to dealing with shapefile tables.
  #try:
  #  q = "DROP TABLE {0};".format(table_name)
  #  print ">", q
  #  db.set_isolation_level(0)
  #  cur.execute(q)
  #except:
  #  print "Nowt to drop."

  try:
    q = "CREATE TABLE {0} ();".format(table_name)
    print ">", q
    db.set_isolation_level(0)
    cur.execute(q)

    cols = {}

    with open(csv_path, "rb") as tidy_csv:
      reader = csv.reader(tidy_csv, delimiter=',')
      for row in reader:
        for field_name in row:
          field_name = field_name.lower()
          cols[field_name] = cols[field_name] + 1 if field_name in cols else 1
          if cols[field_name] > 1:
            field_name += str(cols[field_name])

          q = "ALTER TABLE {0} ADD COLUMN \"{1}\" TEXT;".format(table_name, field_name.lower())
          print ">", q
          db.set_isolation_level(0)
          cur.execute(q)
        break

    q = "COPY {0} FROM STDIN DELIMITERS ',' CSV HEADER;".format(table_name, csv_path)
    print ">", q
    db.set_isolation_level(0)
    with open(csv_path, "rb") as tidy_csv:
      #cur.copy_from(tidy_csv, table_name, ",")
      tidy_csv.readline()
      cur.copy_expert("COPY {0} FROM STDIN WITH (FORMAT CSV)".format(table_name), tidy_csv)
  except:
    print "Table", table_name, "probably exists."
