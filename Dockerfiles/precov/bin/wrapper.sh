#!/bin/sh -x

# this is for the container

database_purifier.py /home/allprot0129.fasta purified_allprot.fasta &&

mkdir proteins &&

protein_extractor.sh purified_allprot.fasta proteins/ &&

# for i in $(ls proteins/); do SUB=$(echo $i | cut -d '.' -f 1); mkdir proteins/$SUB ; mv proteins/$SUB".fasta" proteins/$SUB; done &&

mkdir replacements &&

csv_sorter.sh /home/all_replacements.csv replacements/
