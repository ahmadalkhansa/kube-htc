#database directory inside the image!
#if to construct the image again, remember to install the database too
for sprot in `ls ./database/*.fasta`;
do makeblastdb -in $sprot -dbtype prot ; done
