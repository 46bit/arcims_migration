PSQLUSER=viewers
PSQLDB=viewer_taesp

dropdb $PSQLDB
createdb -O $PSQLUSER $PSQLDB
psql $PSQLDB -c "CREATE EXTENSION postgis; \
  CREATE EXTENSION postgis_topology;"

for shppath in ../arcims_data/taesp_shapefiles/*.shp
do
  shpfile=`basename "$shppath"`
  shp2pgsql -I -s EPSG:4038 "$shppath" "tp_${shpfile%.*}" | psql -U $PSQLUSER $PSQLDB
done

for dbfpath in ../taesp_ahrc_2007/features/dbfs/*.dbf
do
   python dbf_csv_postgres_conversion/dbf2csv.py "$dbfpath"
done

python dbf_csv_postgres_conversion/csvload.py ../taesp_ahrc_2007/features/dbfs

PYTHONPATH=./axl_translator:$PYTHONPATH ./axl_translator/bin/axl_translator ../arcims_data/arcims_mapping/axl/taesp_ahrc_2007_final.axl -o ../arcims_data/taesp_translated

for shppath in ../arcims_data/taesp_translated/*
do
  shpfile=`basename "$shppath"`
  PYTHONPATH=./layer_importer:$PYTHONPATH ./layer_importer/bin/layer_importer taesp_ahrc_2007 postgis_viewer_taesp "taesp_translated/$shpfile" EPSG:4038
done

# @TODO: