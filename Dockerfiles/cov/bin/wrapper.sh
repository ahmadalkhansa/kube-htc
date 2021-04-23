#!/bin/sh -x

# this is for the container

database_purifier.py /home/allprot0129.fasta purified_allprot.fasta &&

mkdir proteins &&

protein_extractor.sh purified_allprot.fasta proteins/ &&

# for i in $(ls proteins/); do SUB=$(echo $i | cut -d '.' -f 1); mkdir proteins/$SUB ; mv proteins/$SUB".fasta" proteins/$SUB; done &&

mkdir replacements &&

csv_sorter.sh /home/all_replacements.csv replacements/ &&

for i in $(ls proteins); do pre_mutational_assignment.py proteins/$i/$i".fasta" proteins/$i/$i".json"; done &&

for i in $(ls proteins/); do prot=$(echo $i | cut -d "/" -f 2); echo $prot; mutational_assignment.py replacements/"$prot"_replacements.csv proteins/$prot/"$prot".json proteins/$prot/"$prot"_replacements.json; done &&

for i in $(ls proteins/); do prot=$(echo $i | cut -d "/" -f 2); echo $i; fasta_mutations.py proteins/$i/"$i"_replacements.json; done
