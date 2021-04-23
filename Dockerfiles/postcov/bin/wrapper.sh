#!/bin/sh -x

PROTEIN=$(ls *.fasta | cut -d "." -f 1)
pre_mutational_assignment.py $PROTEIN.fasta $PROTEIN.json &&

mutational_assignment.py replacements/"$PROTEIN"_replacements.csv $PROTEIN.json "$PROTEIN"_replacements.json &&

fasta_mutations.py "$PROTEIN"_replacements.json
