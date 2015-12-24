PSQLUSER=viewers
PSQLDB=viewer_ww

read -p "Please stop GeoServer and press any key to continue." yn

dropdb $PSQLDB
createdb -O $PSQLUSER $PSQLDB
psql $PSQLDB -c "CREATE EXTENSION postgis; \
  CREATE EXTENSION postgis_topology;"

# All have prj corresponding to EPSG:4278.
#   GEOGCS["GCS_OSGB_1970_SN",
#     DATUM["D_OSGB_1970_SN", SPHEROID["Airy_1830",6377563.396,299.3249646]],
#     PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]
for shppath in ../arcims_data/ww_shapefiles/*.shp
do
  shpfile=`basename "$shppath"`
  shp2pgsql -I -s EPSG:4278 "$shppath" "ww_${shpfile%.*}" > "${shppath%.*}.sql"
  cat "${shppath%.*}.sql" | sed "s/\.0',/',/g" | psql -U $PSQLUSER $PSQLDB
done

for shppath in ../whittlewood_ahrb_2006/features/**/*.shp
do
  shpfile=`basename "$shppath"`
  shp2pgsql -I -s EPSG:4278 "$shppath" "${shpfile%.*}" > "${shppath%.*}.sql"
  cat "${shppath%.*}.sql" | sed "s/\.0',/',/g" | psql -U $PSQLUSER $PSQLDB
done

read -p "Please start GeoServer and press any key to continue." yn

for axlpath in ../arcims_data/arcims_mapping/axl/ww_map*.axl
do
  axlfile=`basename "$axlpath"`
  axlname=${axlfile%.*}
  outpath="../arcims_data/ww_translated/$axlname"

  PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/axl_translator -i "$axlpath" -o "$outpath"

  # Delete everything under ww workspace, then recreate it
  PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/workspace_recreator "$axlname" postgis_viewer_ww --db_name $PSQLDB --db_user $PSQLUSER

  for layerpath in $outpath/*
  do
    echo "$layerpath"
    layerfile=`basename "$layerpath"`
    PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/layer_importer "$axlname" postgis_viewer_ww "$layerpath" EPSG:4278 --db_name $PSQLDB --db_user $PSQLUSER
  done

  for tifpath in ../whittlewood_ahrb_2006/rasters/*.tif
  do
    echo "$tifpath"
    tfwpath="${tifpath%.*}.tfw"
    tiffilename=`basename "${tifpath}"`
    tifname="${tiffilename%.*}"
    layer_id=`PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/axl_layer_id_by_name "$axlpath" "$tiffilename"`
    PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/worldimage_importer "$axlname" "$layer_id" "$tifpath" "$tfwpath" "../whittlewood_ahrb_2006/rasters/27700.prj" "EPSG:27700"
  done

  toclibrarypath="../../../geoserver-2.8.0/webapps/journal/issue19/5/archds-leaflet-mapping/libs/toc.js"
  tocjsonpath="../geoserver-2.8.0/webapps/journal/issue19/5/archds-leaflet-mapping/tocs/$axlname.toc.json"
  tocpath="../geoserver-2.8.0/webapps/journal/issue19/5/archds-leaflet-mapping/tocs/$axlname.toc"

  ./tooling/bin/toc2json.js "$toclibrarypath" "$tocpath" | \
    PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/build_layergroups_from_tocjson "$axlname" -o "$tocjsonpath"

  cat "$tocjsonpath" | PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/update_tocjson_bounds_from_axl \
    -o "$tocjsonpath" \
    -j "$axlpath"
done
