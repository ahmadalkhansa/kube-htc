#!/bin/bash


FASTA_SIZE=$(awk '/^>/ {count++} END{print count}' "$1")

# count the headers and divide the file according to the desired number
awk -v sum=$FASTA_SIZE -v num="$2" 'BEGIN{count=1; multiplier=1}{
if ( count > multiplier * (sum / num)  && $0 ~ /^>/ && multiplier < num ) 
        ++multiplier;
	if ($0 ~ /^>/)
	{
	++count;
	print $0 >> multiplier".fasta";
	}
	else if ($0 !~ /^>/)
        print $0 >> multiplier".fasta";	
}' "$1"

