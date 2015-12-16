prjpath="../arcims_data/taesp_ahrc_2007.prj"
echo 'PROJCS["WGS 84 / UTM zone 36N",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.0174532925199433,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",33],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH],
    AUTHORITY["EPSG","32636"]]' > "$prjpath"

for tifpath in ../arcims_data/tif-tfw/*.tif
do
  tfwpath="${tifpath%.*}.tfw"
  tiffilename=`basename "${tifpath}"`
  tifname="${tiffilename%.*}"
  layer_id=`PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/axl_layer_id_by_name ../arcims_data/arcims_mapping/axl/taesp_ahrc_2007_final.axl "$tiffilename"`
  layer_name="level$(printf %03d $layer_id)"
  PYTHONPATH=./tooling:$PYTHONPATH ./tooling/bin/worldimage_importer taesp_ahrc_2007 "$layer_name" "$tifpath" "$tfwpath" "$prjpath"
done
