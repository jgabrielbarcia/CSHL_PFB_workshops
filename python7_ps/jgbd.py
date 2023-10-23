#! usr/bin/env python3

import sys
import math
import re
from Bio import SeqIO

#input_file = sys.argv[1]
input_file = "Python_07.fasta" 

genes = {}
with open("input_file","r") as fasta_file:
  for line in fasta_file:
    if >(\S+)\s?.* in line
      
    line = line.rstrip()
    gene_id,description = line.split()
    genes[gene_id] = seq

print(genes)

enzymes = {}
with open("/Users/jgabrielbarcia/problemsets/pfb_problemsets/repo1/python7_ps/bionet.txt","r") as enzyme_file:
  for line in enzyme_file:
    line = line.rstrip()
    enzyme_id,cut_site = line.split()
    enzymes[enzyme_id] = cut_site

print(enzymes)

#def reverse_complement(dna_sequence):
  #complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
  #return ''.join([complement[base] for base in dna_sequence[::-1]])

#Iterate through a dictionary:
#for gene_id in genes:
  #seq = genes[gene_id]
  #rev_complement = reverse_complement(seq)
  #print(">",gene_id," reverse complement\n",rev_complement, sep = "")

with open(input_file, 'r') as fasta_file:
  for record in SeqIO.parse(fasta_file, 'fasta'):
    identifier = record.id
    description = record.description
    sequence = record.seq

print('Processing the record {}:'.format(identifier))
print('Its description is: \n{}'.format(description))
amount_of_nucleotides = len(sequence)
print('Its sequence contains {} nucleotides.'.format(amount_of_nucleotides))

#for gene_id in re.findall(r">(\S+)\s?.*", path_to_fasta_file):
 #print(gene_id)

for enzyme_id in enzymes:
  for gene_id in genes:
    enzymes[enzyme_id] = re.sub("(.*)\^(.*)", r"(\1)(\2)", enzymes[enzyme_id])
    if re.match(enzymes[enzyme_id], "^") != None:
      print(gene_id, enzyme_id)
      genes[gene_id] = re.sub(enzymes[enzyme_id], r"\1^\2", genes[gene_id])
      print(gene_id, enzyme_id)
      gene_hit = re.search(enzymes[enzyme_id], genes[gene_id])
      if gene_hit != None:
        print(f"Gene {gene_id} contains cut site for enzyme: {enzyme_id}")


for enzyme_id in enzymes:
  for gene_id in genes:
    enzymes[enzyme_id] = re.sub("(.*)\^(.*)", r"(\1)(\2)", enzymes[enzyme_id])
    if re.match(enzymes[enzyme_id], "^"):
      genes[gene_id] = re.sub(enzymes[enzyme_id], r"\1^\2", genes[gene_id])
      print(gene_id)
