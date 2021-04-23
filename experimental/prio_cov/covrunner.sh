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
        queue 1" > purify.submit; condor_submit purify.submit &&

while [ ! -d proteins ] || [ ! -d replacements ]; do sleep 1; done &&

./postcovrunner.sh
