#!/bin/bash
#before singleline operatin
for file in `ls -1 ./volume/input_fasta/*.fasta`
do
awk -v RS=">" -v FS="\n" '{for(i=2;i<NF;i++) {l+=length($i)}; if(l>40) printf ">%s", $0}' $file  >> "${file%.fasta}_correct.fasta"
done 
