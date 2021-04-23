#!/bin/sh

for i in $(ls proteins/); do
	SIZE=$(awk '{cnt++} END{print cnt}' proteins/$i/$i.fasta)
        echo "Universe = vanilla
        +SingularityImage = \"/home/simages/postcov_latest.sif\"
        executable = execute.sh
        Error = errors/$i.error.\$(cluster)
        Output = outputs/$i.output.\$(cluster)
        Log = logs/$i.log.\$(cluster)
	priority = $SIZE
        should_transfer_files = YES
        transfer_input_files = proteins/$i/$i.fasta, replacements
        transfer_output_files = "$i"_replacements.fasta
	transfer_output_remaps = \""$i"_replacements.fasta = proteins/$i/"$i"_replacements.fasta \"
        queue 1
        " > $i.submit; condor_submit $i.submit; done &

./postcovwait.sh
