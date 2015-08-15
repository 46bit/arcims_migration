#!/usr/bin/env sh

for tocpath in ../taesp_ahrc_2007/*.toc
do
   echo "$tocpath"
   node toc2json.js "$tocpath" > "$tocpath.json"
   #python dbf2csv.py $dbfpath
done
