import sys, csv, psycopg2 as dbapi2

db = dbapi2.connect(database="viewer_taesp", user="viewers", password="qJUdm6JGxYikLXqZusYNvAd8r")
cur = db.cursor()

table_name = sys.argv[1]
key_field_name = sys.argv[2]
tidy_csv_path = sys.argv[3]
field_name_prefix = sys.argv[4] if len(sys.argv) > 4 else ""

with open(tidy_csv_path, "rb") as tidy_csv:
  # Add the first row, the CSV headings, as columns to the database.
  reader = csv.reader(tidy_csv, delimiter=',')
  skipcolumns = []
  for row in reader:
    for field_name in row:
      if field_name != key_field_name:
        try:
          db.set_isolation_level(0)
          cur.execute("ALTER TABLE {} ADD COLUMN {} TEXT;".format(table_name, field_name_prefix + field_name))
        except:
          skipcolumns += [field_name]
          print "Column {} existed. Presumably.".format(field_name)
    break

  tidy_csv.seek(0)

  # Add the data from each record to the database.
  dictreader = csv.DictReader(tidy_csv, delimiter=',')
  for dictrow in dictreader:
    key_field_value = dictrow[key_field_name]
    print "| {}={}".format(key_field_name, key_field_value)
    for field_name, field_value in dictrow.items():
      if field_name != key_field_name and field_name not in skipcolumns:
        print "|+ {}={}".format(field_name_prefix + field_name, field_value)
        q = "UPDATE {} SET {}=%s WHERE {}=%s;".format(table_name, field_name_prefix + field_name, key_field_name)
        cur.execute(q, (field_value, key_field_value))
      else:
        print "|= {}={}".format(field_name, field_value)
