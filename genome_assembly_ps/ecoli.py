#! usr/bin/env python3

import sys
import re
import math

input_file = sys.argv[1]
contigs = {}
other_info = []

with open(input_file,"r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        if ">" in line:
            other_info = re.split(r" ", line)
            contig_id = other_info[0]
            contigs[contig_id] = ''
        else:
            contigs[contig_id] += line

sequences = contigs.values()

print(f'This file has {len(contigs)} contigs.\nThe shortest contig is {min(len(sequence) for sequence in sequences)} nucleotides long.\nThe longest contig is {max(len(sequence) for sequence in sequences)} nucleotides long.\nThe total contig length is {len(contigs[contig_id])} nucleotides.')
