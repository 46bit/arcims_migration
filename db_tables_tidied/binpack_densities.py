import sys, csv, string, psycopg2 as dbapi2

def float_or_zero(v):
  return 0.0 if len(string.strip(str(v))) == 0 else float(v)

db = dbapi2.connect(database="viewer_taesp", user="viewers", password="qJUdm6JGxYikLXqZusYNvAd8r")
cur = db.cursor()

table_name = sys.argv[1]
density_field_name = sys.argv[2]
bin_count = int(sys.argv[3])

cur.execute("SELECT COUNT(*) FROM {} WHERE {} > 0;".format(table_name, density_field_name))
bin_capacity = cur.fetchone()[0] / bin_count

print "Bin #0 {} range: (-1, 0)".format(density_field_name)

for bin_number in range(0, bin_count):
  q = """
  SELECT MIN({0}), MAX({0}) FROM
    (SELECT {0}
      FROM {1}
      WHERE {0} > 0
      ORDER BY {0} ASC
      LIMIT {2}
      OFFSET {2}*{3}) AS p;
  """.format(density_field_name, table_name, bin_capacity, bin_number)
  cur.execute(q)

  bin_density = cur.fetchone()
  bin_density_min = bin_density[0]
  bin_density_max = bin_density[1]
  print "Bin #{} {} range: ({}, {})".format(bin_number + 1, density_field_name, bin_density_min, bin_density_max)

#####

# For GeoServer SLD Styling

print """
<PolygonSymbolizer>
  <Fill>
    <CssParameter name="fill">
      <ogc:Function name="Categorize">
        <ogc:PropertyName>{0}</ogc:PropertyName>

        <!-- Bin #0 {0} range: (-1, 0) -->
        <ogc:Literal>#</ogc:Literal> <ogc:Literal>-1</ogc:Literal>
        <ogc:Literal>#</ogc:Literal> <ogc:Literal>0</ogc:Literal>
""".format(density_field_name)

for bin_number in range(0, bin_count):
  q = """
  SELECT MIN({0}), MAX({0}) FROM
    (SELECT {0}
      FROM {1}
      WHERE {0} > 0
      ORDER BY {0} ASC
      LIMIT {2}
      OFFSET {2}*{3}) AS p;
  """.format(density_field_name, table_name, bin_capacity, bin_number)
  cur.execute(q)

  bin_density = cur.fetchone()
  bin_density_min = bin_density[0]
  bin_density_max = bin_density[1]

  print """        <!-- Bin #{0} {1} range: ({2}, {3}) -->
        <ogc:Literal>#</ogc:Literal> <ogc:Literal>{2}</ogc:Literal>
        <ogc:Literal>#</ogc:Literal> <ogc:Literal>{3}</ogc:Literal>
""".format(bin_number + 1, density_field_name, bin_density_min, bin_density_max)


print """      </ogc:Function>
    </CssParameter>
  </Fill>
</PolygonSymbolizer>"""
