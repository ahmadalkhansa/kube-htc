#!/bin/sh -x

HEAD=$(head -n 1 $1)

awk -v outdir=$2 -F ":" 'BEGIN{OFS=FS}{
  if (NR!=1) print $0 >> outdir"pre,"$1"_replacements.csv";
  }' "$1" &&

for i in $(ls $2pre*); do FINAL=$(echo $i | cut -d "," -f 2); echo $HEAD >> $2$FINAL; cat $i >> $2$FINAL; rm $i; done