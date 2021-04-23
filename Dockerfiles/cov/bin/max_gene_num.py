#!/usr/bin/python3

import json
import sys

def max_id(json_file):
	"""
	extract ids with max number of sequences
	:param json_file:
	:return: new json
	"""
	max = 10
	json_ouput = {}
	for i in json_file:
		if len(json_file[i]) == max:
			json_ouput[i] = json_file[i]
		elif len(json_file[i]) > max:
			#qjson_ouput = {}
			json_ouput[i] = json_file[i]

	return json_ouput

if __name__=="__main__":
	json_database = open(sys.argv[1], "r")
	output_json = open(sys.argv[2], "w+")
	json_load = json.load(json_database)
	tobe_dumped = max_id(json_load)
	json_database.close()
	json.dump(tobe_dumped, output_json)
	output_json.close()