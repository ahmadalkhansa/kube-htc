#!/usr/bin/python3

import sys

def purifier(database, pure):
	'''
	remove sequences with unidentified residues
	'''
	headers =""
	with open(database) as seqs:
		for i in seqs:
			line = i.strip()
			if line[0] == ">":
				headers=line
			else:
				if "X" in line: # or line[0] != "M" or line[-1] != "*":
					headers=""
				else:
					pure.write(headers+"\n"+line[:-1]+"\n")
	seqs.close()
	pure.close()

	return "purification success"


if __name__ == "__main__":
	input_database = sys.argv[1]
	purified_database = open(sys.argv[2], "a+")
	clear_output = purifier(input_database, purified_database)
