PSQLUSER=viewers
PSQLDB=viewer_taesp

read -p "Please stop GeoServer and press any key to continue." yn

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

PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/axl_translator -i ../arcims_data/arcims_mapping/axl/taesp_ahrc_2007_final.axl -o ../arcims_data/taesp_translated

read -p "Please start GeoServer and press any key to continue." yn

# Delete everything under taesp_ahrc_2007 workspace, then recreate it
PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/workspace_recreator taesp_ahrc_2007 postgis_viewer_taesp --db_name $PSQLDB --db_user $PSQLUSER

for layerpath in ../arcims_data/taesp_translated/*
do
  layerfile=`basename "$layerpath"`
  PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/layer_importer taesp_ahrc_2007 postgis_viewer_taesp "../arcims_data/taesp_translated/$layerfile" EPSG:4038 --db_name $PSQLDB --db_user $PSQLUSER
done

for tiffpath in ../taesp_ahrc_2007/rasters/*.tif
do
  tifffile=`basename "$tiffpath"`
  PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/geotiff_importer taesp_ahrc_2007 "${tifffile%.*}" "$tiffpath"
done

prjpath="../arcims_data/taesp_ahrc_2007.prj"
echo 'PROJCS["WGS_1984_UTM_Zone_26N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",-27],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["Meter",1]]' > "$prjpath"

for tifpath in ../arcims_data/tif-tfw/*.tif
do
  echo "$tifpath"
  tfwpath="${tifpath%.*}.tfw"
  tiffilename=`basename "${tifpath}"`
  tifname="${tiffilename%.*}"
  layer_id=`PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/axl_layer_id_by_name ../arcims_data/arcims_mapping/axl/taesp_ahrc_2007_final.axl "$tiffilename"`
  PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/worldimage_importer taesp_ahrc_2007 "$layer_id" "$tifpath" "$tfwpath" "$prjpath" "EPSG:32626"
done
