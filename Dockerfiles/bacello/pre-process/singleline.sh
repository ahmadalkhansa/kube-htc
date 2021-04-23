#!/bin/bash
for file in `ls -1 ./volume/input_fasta/*_correct.fasta`
do 
echo $file
if [[ ${file} == *"_singleline.fasta"* ]] 
	then
	: 
elif [[ ! -s ${file} ]]
	then 
	rm $file
else	
	cat $file | awk '/^>/ { if(NR>1) print "";  printf("%s\n",$0); next; } { printf("%s",$0);}  END {printf("\n");}' >> "${file%_correct.fasta}_singleline.fasta"
	#cat $file | awk -F '|' '/^>/ {F=sprintf("%s.fasta",$2); print > F;next;} {print >> F;}' < "${file%.fasta}_singleline.fasta"

fi 
done 
