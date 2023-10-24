#! usr/bin/env python3

import sys
import math
import re
from Bio import SeqIO

#COUNTING THE SEQUENCES
#Using biopython
record_ID = [record.id for record in SeqIO.parse("uniprot_sprot.fasta", "fasta")]
print("Number of sequences, biopython:", len(record_ID))

#Or, with regular Python:
fh = open("uniprot_sprot.fasta")
n = 0
for line in fh:
    if line.startswith(">"):
        n += 1
print("Number of sequences, loop:",n)
fh.close()

#Or:
num = len([1 for line in open("uniprot_sprot.fasta") if line.startswith(">")])
print("Number of sequences, list comp:",num)

#COUNTING DESCRIPTIONS

record_descr = [record.description for record in SeqIO.parse("uniprot_sprot.fasta", "fasta")]
print(record_descr[0:20])

#Using regular expressions, extract just the genus and species and count the number of sequences present for that genus/species combination

species = [species.group for x in record_descr[x] if re.search(r'OS=(.*) OX=', record_descr)]

i = 0
species = []
for line in re.search(r'OS=(.*)\s+(\(.*?\))?OX=', record_descr):
  species += species.group(i)
  i + 1
  

