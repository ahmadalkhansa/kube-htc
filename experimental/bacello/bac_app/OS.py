#!/usr/bin/env python3

import os
import sys
#import requests
#import urllib.request
#to get url interrogation on given request
from urllib.request import urlopen

def fastareader(fasta):
	with open(fasta) as f:
		for line in f:
			line = line.strip()
						#print (line)
						#ids = ["OS", "OX"]
			if line.startswith('>'):
						   # if any(ids in line for ids in ids): 
						   #flag=None
						   #OX=""
				#print (line)
				if "OS" in line:
					species_id = line.split("OS")[1].split("=")[1].split(" ")[0:2]
					#print (species_id)
					species_name = " ".join(species_id)
						   #print (species_name)
					os.environ["SPECIES_NAME"] = species_name
								   #OS=str(species_name)
								   #flag=1
						   #print (species_ids)
				elif "OX" in line: #OS not in identifier line, using TAX ID OX
					species_id = line.split("OX")[1].split("=")[1].split(" ")[0]
					#print (species_id)
								   #OX=str(species_id)
					os.environ["TAXONOMY_ID"] = species_id
	
#identifier = ""
	if "SPECIES_NAME" in os.environ:
		identifier = (os.environ.get("SPECIES_NAME"))
	else:
		identifier = (os.environ.get("TAXONOMY_ID"))

	#print (identifier)
	
	return identifier
	#print(os.environ.get("TAXONOMY_ID"))


def get_rest_recognition(identifier):
    http_name = "https://www.ebi.ac.uk/ena/taxonomy/rest/scientific-name/"
    #http2 = "http://www.ebi.ac.uk/ena/data/view/Taxon:"
    http_id = "https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/"
    #print(os.environ.get("TAXONOMY_ID"))
    #print(os.environ.get("SPECIES_NAME"))
    kingdom=None
    #print (identifier)
    if os.environ.get("SPECIES_NAME") == identifier:
        species_name = identifier
        params = species_name.split(" ")[0] + "%20" + species_name.split(" ")[1]
        #format = "&display=xml"     to use with http2
        r = urlopen(http_name+str(params)).read()
        dec_r = r.decode("utf-8") 
        s = dec_r.split(",")
        for line in s:
            if "lineage" in line:
                lineage_line = line
                if "Metazoa" in lineage_line:
                    #print (species_name,": Animal")
                    kingdom = "Animal"
                elif "Fungi" in lineage_line:
                    #print (species_name,": Funghi")
                    kingdom = "Fungi"
                elif ("Viridiplantae") in lineage_line:
                    #print (species_name,": Piante")
                    kingdom = "Plant"
                else:
                    print ("No Taxonomy identified.")
#decode of output of http2 too complicated! using this database is the best idea. 
    elif os.environ.get("TAXONOMY_ID") == identifier :
        tax_id = identifier
        r = urlopen(http_id+tax_id).read()
        dec_r = r.decode("utf-8")
        s = dec_r.split(",")
        for idn in s:
            if "lineage" in idn:
                lineage_line = line
                if "Metazoa" in lineage_line:
                   #print (species_name,": Animal")
                    kingdom = "Animal"
                elif "Fungi" in lineage_line:
                    #print (species_name,": Funghi")
                    kingdom = "Fungi"
                elif ("Viridiplantae") in lineage_line:
                    #print (species_name,": Piante")
                    kingdom = "Plant"
                else:
                    print ("No Taxonomy identified.")

    else:
        raise EnvironmentError("Failed because Species Name or Taxonomy ID are not set.")

    return (kingdom)    

if __name__ == '__main__':

	fastafile = sys.argv[1]
	#print (fastafile)
	if fastafile.endswith('_singleline.fasta'):
				#print ("OK")
		id = fastareader(fastafile)
		#print (id)
		if id != None: 
			kingdom = get_rest_recognition(id)
			print (kingdom)
		else:
			print ("No identification possible, check the fasta file!")
				#print('OK')
				#return kingdom
			#print (kingdom)
