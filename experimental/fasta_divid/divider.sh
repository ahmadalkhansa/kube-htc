#!/bin/bash


FASTA_SIZE=$(awk '/^>/ {count++} END{print count}' "$1")

# count the headers and divide the file according to the desired number
awk -v sum=$FASTA_SIZE -v num="$2" '{ 
	if ($0 ~ /^>/)
{
	++count;
	print $0 >> num".fasta";
}
	if (sum / count == num && num != 1)
{
	--num;
	print $0 >> num".fasta";
}
	else if ($0 !~ /^>/)
	print $0 >> num".fasta";
}' "$1"

