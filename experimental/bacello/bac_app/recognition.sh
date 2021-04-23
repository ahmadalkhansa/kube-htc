#!/bin/bash
#Checking the output of the Python code for the recognition of the kingdom: 
#FOR EVERY FILE IN THE INPUT VOLUME (SO FASTA FILE):
shopt -s extglob

#ls /home/input_fasta
pwd

for FASTA_FILE in `ls ./volume/input_fasta/*_singleline.fasta`
do 
kingdom=$(./OS.py $FASTA_FILE)
#echo $kingdom
K=""
#s=${s##*/}
#filename=$(echo "${FASTAFILE%_*}")
filename=$(basename "$FASTA_FILE" _singleline.fasta)
#echo $filename
PSSM_FILE="${filename}.pssm"
#PSSM_FILE=$filename + ".pssm"
#echo $PSSM_FILE
if [[ $(find ./volume/input_pssm -name "$PSSM_FILE") ]]; then 
	#if [[ -e ~/ ./input_pssm/$PSSM_FILE  ]]; then 
	echo "PSSM file exists, can carry on."
	echo $kingdom 
	if [[ $kingdom == "Animal" ]]; then 
		echo "Kingdom recognized as Animal; launghing Bacello..."
		K="A"
		python3 ../bacello/bacello.py -f $FASTA_FILE -p ./volume/input_fasta/$PSSM_FILE -k $K
	fi
	if [[ $kingdom == "Fungi" ]]; then 
		echo "Kingdom recognized as Fungi; launghing Bacello..."
		K="F"
        	python3 ../bacello/bacello.py -f $FASTA_FILE -p ./volume/input_fasta/$PSSM_FILE -k $K
	fi
	if [[ $kingdom == "Plant" ]]; then 
        	echo "Kingdom recognized as Plant; launghing Bacello..."
		K="P"
        	python3  ../bacello/bacello.py -f $FASTA_FILE -p ./volume/input_fasta/$PSSM_FILE -k $K
	fi
	if [[ $kingdom == "None" ]]; then
		echo "No kingdom was recognized, impossible to launch Bacello application."
	fi
	
else
	echo "No PSSM file was detected, can not carry on the operation. Breaking Bacello." 
fi

done
