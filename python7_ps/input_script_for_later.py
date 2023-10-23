#! usr/bin/env python3

import sys
import math
import re

input_file = ''
genes = {}
other_info = []

try:
  input_file = sys.argv[1]
  print("User provided file name:" , input_file)
  if not re.match("^.*(\.fa|\.fasta)$", input_file):
    raise ValueError("This doesn't look like a fasta file")
  with open(input_file,"r") as fasta_file:
    for line in fasta_file:
      line = line.rstrip()
      if ">" in line:
        other_info = re.split(r" ", line)
        gene_id = other_info[0]
        genes[gene_id] = ''
      else:
        genes[gene_id] += line
except IndexError:
  print("Please provide a fasta file")
except IOError as ex:
  print("Error reading fasta file:" , input_file , ': ' , ex.strerror)
