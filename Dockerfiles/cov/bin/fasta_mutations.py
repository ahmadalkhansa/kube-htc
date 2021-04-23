#!/usr/bin/python3

import sys
import re
import json

def fasta_builder(mutational_json, file_writable, protein_name):
	'''
	create a fasta that sums up the mutations
	:param mutational_json:
	:return:
	'''
	orf = protein_name
	if orf == "NS3":
		orf = "ORF_3a"
	elif re.match("NS[0-9]", orf):
		prot = orf.split("S")[1]
		orf = "ORF_"+prot

	for seq in mutational_json:
		header = ">"+protein_name+"|"+orf+"|"+",".join(mutational_json[seq]["replacements"])+"|"+\
				 mutational_json[seq]["ids"][0]+"|"+str(len(mutational_json[seq]["ids"]))+"\n"
		file_writable.write(header+seq+"\n")

	return

if __name__=="__main__":
	name = sys.argv[1].split("/")[1]
	name = name.split("_")[0]
	input_json = open(sys.argv[1], "r")
	input_json = json.load(input_json)
	output_fasta = open(sys.argv[1].split(".")[0]+".fasta", "a+")
	fasta_builder(input_json, output_fasta, name)
