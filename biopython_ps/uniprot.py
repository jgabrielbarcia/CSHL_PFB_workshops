#! usr/bin/env python3

import sys
import math
import re
from Bio import SeqIO

#COUNTING THE SEQUENCES

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

print(record_ID[0:10])

#COUNTING DESCRIPTIONS

record_descr = [record.description for record in SeqIO.parse("uniprot_sprot.fasta", "fasta")]

print(record_descr[0:20])


