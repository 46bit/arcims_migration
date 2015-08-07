import sys, csv, string, psycopg2 as dbapi2

def float_or_zero(v):
  return 0.0 if len(string.strip(str(v))) == 0 else float(v)

db = dbapi2.connect(database="viewer_taesp", user="viewers", password="qJUdm6JGxYikLXqZusYNvAd8r")
cur = db.cursor()

table_name = sys.argv[1]
key_field_name = sys.argv[2]
count_field_name = sys.argv[3]
area_field_name = sys.argv[4]
density_field_name = sys.argv[5]

try:
  db.set_isolation_level(0)
  cur.execute("ALTER TABLE {} ADD COLUMN {} TEXT;".format(table_name, density_field_name))
except:
  print "Column {} existed. Presumably.".format(density_field_name)

cur.execute("SELECT {}, {}, {} FROM {} ORDER BY {};".format(key_field_name, count_field_name, area_field_name, table_name, key_field_name))
for row in cur.fetchall():
  key_field_value = row[0]
  count_field_value = float_or_zero(row[1])
  area_field_value = float_or_zero(row[2])

  print "| {}={}".format(key_field_name, key_field_value)
  print "|= {}={}".format(count_field_name, count_field_value)
  print "|= {}={}".format(area_field_name, area_field_value)

  if area_field_value > 0.0:
    density = str(count_field_value / area_field_value)
    print "|+ {}={}".format("density", density)
  else:
    density = -1.0
    print "|~ {}={}".format("density", density)

  cur.execute("UPDATE {} SET {} = %s WHERE {} = %s;".format(table_name, density_field_name, key_field_name), (density, key_field_value))
