#!/bin/bash
#ls 
#pwd 
#ls /home 
#ls /home/predgpi_app/
#ls /home/predgpi_app/input/
for file in `ls volume/input/*_stdout`; do mv $file volume/output/ ; done
