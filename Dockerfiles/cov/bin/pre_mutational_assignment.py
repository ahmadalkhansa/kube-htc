#!/usr/bin/python3

import sys
import json

def indexer(protein_file):
	'''
	create a json for proteins
	:param protein_file:
	:return:
	'''
	output_json = {}
	with open(protein_file, "r") as prep:
		header = ""
		for i in prep:
			if i[0] == ">":
				header = i.split("|")[3]
			else:
				sequence = i.strip()
				if sequence not in output_json:
					output_json[sequence] = {"ids":[header]}
				else:
					output_json[sequence]["ids"].append(header)

	return output_json

if __name__=="__main__":
	protein = sys.argv[1]
	json_file = open(sys.argv[2], "w+")
	result = indexer(protein)
	json.dump(result, json_file)