#!/usr/bin/env sh

for dbfpath in ../dbfs/*.dbf
do
   echo "$dbfpath"
   python dbf2csv.py $dbfpath
done
