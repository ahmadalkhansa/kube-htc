#!/usr/bin/env python3

import sys
infile = open(sys.argv[1])
outfile = []

#def separator(infile,outfile):
for line in infile:
    if line.startswith(">"):
        if (outfile != []): 
            outfile.close()
        genename = line.strip().split('|')[1].split('.')[0]
        filename = genename+".fasta"
        outfile = open(filename,'w')
        outfile.write(line)
    else:
        outfile.write(line)
outfile.close()


'''
if __name__ == "__main__":
                fastafile = sys.argv[1]
                print (fastafile)
                if fastafile.endswith('.fasta'):
                                #print ("OK")
                                outfile = []
                                separator(fastafile, outfile)'''

