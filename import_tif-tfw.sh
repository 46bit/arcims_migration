prjpath="../arcims_data/taesp_ahrc_2007.prj"
echo 'PROJCS["WGS_1984_UTM_Zone_36N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",33.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]' > "$prjpath"

for tifpath in ../arcims_data/tif-tfw/*.tif
do
  tfwpath="${tifpath%.*}.tfw"
  tifname=`basename "${tifpath%.*}"`
  PYTHONPATH=./layer_importer:$PYTHONPATH ./layer_importer/bin/worldimage_importer taesp_ahrc_2007 "$tifname" "$tifpath" "$tfwpath" "$prjpath"
done
