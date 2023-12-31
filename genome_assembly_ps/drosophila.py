#! usr/bin/env python3

import sys
import re
import math

input_file = sys.argv[1]
genes = {}
other_info = []

with open(input_file,"r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        if ">" in line:
            other_info = re.split(r" ", line)
            gene_id = other_info[0]
            genes[gene_id] = ''
        else:
            genes[gene_id] += line

print(f'This file has {len(genes)} genes.')


nucleotides = ['A','T','C','G','N']
#Genes first because we're organizing by gene
for gene_id in genes:
    for up_nucleotide in nucleotides:
        up_count = genes[gene_id].count(up_nucleotide)
        print(f"There are {up_count} '{up_nucleotide}'s in {gene_id}\n")
nucleotides2 = ['a','t','c','g','n']
for gene_id in genes:
    for lo_nucleotide in nucleotides2:
        lo_count = genes[gene_id].count(lo_nucleotide)
        print(f"There are {lo_count} '{lo_nucleotide}'s in {gene_id}\n")
