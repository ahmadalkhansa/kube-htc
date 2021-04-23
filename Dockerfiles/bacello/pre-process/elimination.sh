#!/bin/bash
#after the rotation, the files are in this directory
for file in `ls ./volume/input_fasta/*.fasta`
do 
	count=$(grep -Fo '>' $file | wc -l)
	if [[ $count -gt 1 ]] 
		then 
		rm $file
	fi
done
