#! usr/bin/env python3

import sys
import math

genes = {}
with open("Python_06.seq.txt","r") as hw_file:
  for line in hw_file:
    line = line.rstrip()
    gene_id,seq = line.split()
    genes[gene_id] = seq
    
def reverse_complement(dna_sequence):
  complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
  return ''.join([complement[base] for base in dna_sequence[::-1]])

#Iterate through a dictionary:
for gene_id in genes:
  seq = genes[gene_id]
  rev_complement = reverse_complement(seq) 
  print(">",gene_id," reverse complement\n",rev_complement, sep = "")

#Make sure to print the output in FASTA format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.

