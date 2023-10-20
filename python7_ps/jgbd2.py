#! usr/bin/env python3

import sys
import math
import re

###

#Read bionet file into dictionary of enzyme_id : cut_site
path_to_bionet_file = "/Users/jgabrielbarcia/problemsets/pfb_problemsets/repo1/python7_ps/bionet.txt"
enzymes = {}
count = 0

with open(path_to_bionet_file, "r") as bionet:
  for line in bionet:
    line = line.rstrip()
    if count < 10:
      count += 1     
      continue
    elif line == "":
      continue
    else:
      enzyme_id,cut_site = re.split(r"\s\s+", line)
      enzymes[enzyme_id] = cut_site 
      count += 1

#Get fasta file and create dictionary of gene_id : seq
#input_file = sys.argv[1]
input_file = "/Users/jgabrielbarcia/problemsets/pfb_problemsets/repo1/python7_ps/Python_07.fasta"
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

#Convert enzyme cut_sites to ACTG format (compatible with fasta file)
def RE_function(seq):
    base_dict = {'^':'^','A':'A', 'T':'T', 'C':'C', 'G':'G', 'N':'[ATCG]', 'R':'[GA]', 'Y':'[TC]', 'K':'[GT]', 'M':'[AC]', 'S':'[GC]', 'W':'[AT]', 'B':'[GTC]', 'D':'[GAT]', 'H':'[ACT]', 'V':'[GCA]'}
    return ''.join([base_dict[nt] for nt in seq])

for enzyme_id in enzymes:
  enzymes[enzyme_id] = RE_function(enzymes[enzyme_id])
  #print(enzymes[enzyme_id])

#Put whatever is before and after hats in parenthesis so they can be found in gene sequences
for enzyme_id in enzymes:
  for gene_id in genes:
    enzymes[enzyme_id] = re.sub("(.*)\^(.*)", r"(\1)(\2)", enzymes[enzyme_id])
    if re.match(r"\(", enzymes[enzyme_id]):  
      genes[gene_id] = re.sub(enzymes[enzyme_id], r"\1^\2", genes[gene_id])
      gene_hit = re.search(enzymes[enzyme_id], genes[gene_id])
      if gene_hit:
        print(f"Gene {gene_id} contains cut site for enzyme: {enzyme_id}")

"""
#For every time an enzyme matches a sequence, report both

#enzymes = {'enzyme1':'(AA)(GTGAT)', 'enzyme2':'ATGCT'}    
#genes = {'gene1':'TCGGSCTAAAGTGAT','gene2':'AGATGATTAGAT'}

pattern_test = r'(AA)(GTGAT)'
#Insert hats into gene sequences
for gene_id in genes:
   genes[gene_id] = re.sub(pattern_test, r"\1^\2", genes[gene_id])
   print(genes[gene_id])

for gene_id in genes:
  for enzyme_id in enzymes:
    gene_hit = re.search(enzymes[enzyme_id], genes[gene_id])
    seq_list = re.split("\^", genes[gene_id])
    print("Unsorted Fragments:", "\t".join(seq_list))
    if gene_hit != None:  
     print(f"Gene {gene_id} contains cut site for enzyme: {enzyme_id}")

for header in fasta_dict:
   fasta_dict[header] = re.sub(enzymes[my_enzyme] , r"\1^\2" , fasta_dict[header])


# print out FASTA dictionary
for header in fasta_dict:
  print("SeqName:", header)
  print("Sequence:", fasta_dict[header])
  seq_list = re.split("\^", fasta_dict[header])
  print("Unsorted Fragments:", "\t".join(seq_list))
  sorted_seqs = sorted(seq_list, key=len, reverse=True)
  print("Number of Fragments:", len(seq_list))
  print("Sorted Fragments:", "\t".join(sorted_seqs))

"""
