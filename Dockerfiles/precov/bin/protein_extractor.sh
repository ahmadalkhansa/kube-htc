#!/bin/sh -x

Help()
{
	echo "extractor.sh <database> <output directory>"
}

awk -v outputdir="$2" -F "|" 'BEGIN{filename="";OFS=FS;}{
	if ($1 ~ /^>/)
		{
		gsub(/>/, "", $1);
		filename=outputdir $1".fasta";
		print ">"$0 >> filename;
		}
	else if ($0 !~ /^>/)
	  {
		print $0 >> filename
		close(filename)
		}
	}' "$1"
		

for i in $(ls "$2"*.fasta); do file=$(echo $i | cut -d "." -f 1); mkdir $file; mv $i $file; done
