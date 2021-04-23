#!/usr/bin/python3

import sys

def organizer(initial_fasta):
	'''
	remove redundencies in sequences
	'''
	genes = {}
	with open(initial_fasta) as initial:
		for i in initial:
			if i[0] == ">":
				headers.append(i)
			else:
				if i in sequences:
					del headers[-1]
				else:
					sequences.append(i)

	return headers, sequences

def filter(heads, seqs):
	'''
	remove sequences with undetermined residues
	'''
	filtered_output=[]
	for i in range(0, len(seqs)):
		if "X" in seqs[i]:
			continue
		else:
			filtered_output.append(heads[i])
			filtered_output.append(seqs[i])
	return "".join(filtered_output)

if __name__=="__main__":
	input_file = sys.argv[1]
	first, second = organizer(input_file)
	output_file = open(sys.argv[2], "w+")
	output_file.write(filter(first, second))
	output_file.close()
