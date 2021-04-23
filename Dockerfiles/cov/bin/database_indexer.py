#!/usr/bin/python3

import sys
import json

def indexer(purified_database):
	'''
	index the purified database
	:param purified_database:
	:return: json file
	'''
	output_json = {}
	i = 0
	with open(purified_database) as fasta:
		for line in fasta:
			i += 1
			if line[0]==">":
				header = line.split("|")
				ident = header[3]
				gene = header[0][1:]
				if gene not in output_json:
					output_json[gene] = {}
				output_json[gene][ident] = i

	return output_json

if __name__=="__main__":
	input_database = sys.argv[1]
	output_json = indexer(input_database)
	json_database = open(sys.argv[2], "w+")
	json.dump(output_json, json_database)
	json_database.close()