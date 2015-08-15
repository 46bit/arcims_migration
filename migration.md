# ArcIMS Migration Tools

## DBF to CSV and PostGIS
Go to the directory with your DBFs in,

``` sh
cd dbf_csv_postgres_conversion
```

Convert them into CSVs,

``` sh
arcims_migration/dbf_csv_postgres_conversion/dbf2csvall.sh
```

Import into Postgres as tables of TEXT fields,
``` sh
python arcims_migration/dbf_csv_postgres_conversion/csvload.py
```

## Add CSV fields to an existing database
See `db_tables_tidied/add_fields.py`.

## Shapefile to PostGIS
``` sh
for a in *.shp
do
  shp2pgsql -I -s EPSG:4038 "$a" "tp_${a%.*}" | psql -U viewers viewer_taesp
done
```

## AXL to SQL/SLD/CSS
Convert each `<LAYER>` entry in an ARCIMS `.axl` file into:

* An `.sql` file containing the query to get the appropriate data.
* An `.sld` file containing SLD styles to format the layer on a modern mapping server (in particular, GeoServer).
* *DEPRECATED*: A `.css` file containing CSS styles to format the layer. This relied on a GeoServer CSS extension that doesn't actually work very well.

Specify the directory to create and fill with these files using the `-o` option.

``` sh
./axl_translator/bin/axl_translator ../arcims_data/arcims_mapping/axl/taesp_ahrc_2007_final.axl -o taesp_translated
```
