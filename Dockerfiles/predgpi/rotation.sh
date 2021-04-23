#!/bin/bash
#mv ./volume/input_fasta/*.pssm ./volume/output
for file in  `ls volume/input/*.fasta`; do separator.py $file; done
