#!/usr/bin/python3

import sys
import pandas as pd
import json
import re

def replacementer(input_csv, json_index):
	'''
	writes replacements
	'''
	i = 0
	output_json = {}
	try:
		df = pd.read_csv(input_csv, index_col=0)
		for seq in json_index:
			i += 1
			output_json[seq] = json_index[seq]
			output_json[seq]["replacements"] = []
			for index,row in df.iterrows():
				num = int(row["codonNumber"])
				try:
					if row["replacementAminoAcid"] == seq[num-1]:
						output_json[seq]["replacements"].append(row["replacement"])
				except IndexError:
					if row["replacementAminoAcid"] == "*" and num == len(seq) + 1:
						output_json[seq]["replacements"].append(row["replacement"])
		print(i)
		return output_json
	except:
		sol = open(sys.argv[2].split(".")[0]+"_replacements.fasta", "w+")
		sol.write("! NO REPLACEMENT FILE")
		sol.close

if __name__=="__main__":
	replac_file = sys.argv[1]
	protein = sys.argv[2].split(".")[0]
	# protein = protein.split(".")[0]
	if protein == "NS3":
		replac_file = sys.argv[1].split("/")[0]+"/ORF_3a_replacements.csv"
	elif protein == "Spike":
		replac_file = sys.argv[1].split("/")[0] + "/S_replacements.csv"
	elif re.match("NS[0-9]", protein):
		replac_file = sys.argv[1].split("/")[0]+"/ORF_"+protein.split("S")[1]+"_replacements.csv"
	database_seqs = open(sys.argv[2], "r")
	database_seqs = json.load(database_seqs)
	replacements = replacementer(replac_file, database_seqs)
	replac_output = open(sys.argv[3], "w+")
	json.dump(replacements, replac_output)
