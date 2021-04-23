#!/bin/sh

mkdir errors &&
mkdir outputs &&
mkdir logs &&

echo "Universe = vanilla 
	+SingularityImage = \"/home/simages/precov_latest.sif\" 
        executable = execute.sh 
        Error = error 
        Output = output 
        Log = log 
        should_transfer_files = YES 
        #transfer_input_files = proteins/ 
        transfer_output_files = proteins, replacements 
        when_to_transfer_output = ON_EXIT_OR_EVICT 
        #initialdir = /home/jovyan/work/experimental/cov/ 
        queue 1" > purify.submit; condor_submit purify.submit

while [ ! -d proteins ] || [ ! -d replacements ]; do sleep 1; done &&

for i in $(ls proteins/); do
        echo "Universe = vanilla
        +SingularityImage = \"/home/simages/postcov_latest.sif\"
        executable = execute.sh
        Error = errors/$i.error.\$(cluster)
        Output = outputs/$i.output.\$(cluster)
        Log = logs/$i.log.\$(cluster)
        should_transfer_files = YES
        transfer_input_files = proteins/$i/$i.fasta, replacements
        transfer_output_files = "$i"_replacements.fasta
	transfer_output_remaps = \""$i"_replacements.fasta = proteins/$i/"$i"_replacements.fasta \"
        queue 1
        " > $i.submit; condor_submit $i.submit; done &

for i in $(ls proteins/); do
        while [ ! -f proteins/$i/"$i"_replacements.fasta ]
        do
                sleep 1
        done
done

