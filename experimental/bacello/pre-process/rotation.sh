#!/bin/bash
#mv ./volume/input_fasta/*.pssm ./volume/output
for file in  `ls ./volume/*.fasta`; do ./separator.py $file; ls ; done 
#splitting multifasta into single fastas, they are now in the directory home when the script is launched
