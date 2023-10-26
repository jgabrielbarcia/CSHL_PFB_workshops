#! usr/bin/env Python3

import sys
import re
import math
from Bio import SeqIO

#Functions

def parse_fasta_file_with_biopython(fasta_file):
    gene_sequences = {}

    for record in SeqIO.parse(fasta_file, "fasta"):
        gene_id = record.id
        sequence = str(record.seq)
        nucleotide_counts = sequence_to_dict(sequence)
        gene_sequences[gene_id] = nucleotide_counts

    return gene_sequences

def sequence_to_dict(sequence):
    nucleotide_counts = {}
    for nucleotide in sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
        else:
            nucleotide_counts[nucleotide] = 1
    return nucleotide_counts

#Main

def main():

    input_fasta = sys.argv[1]

    gene_sequences = parse_fasta_file_with_biopython(input_fasta)

    #Print the results
    print("Gene ID\tA_count\tT_count\tG_count\tC_count")
    for gene_id, nucleotide_counts in gene_sequences.items():
        a_count = nucleotide_counts.get('A', 0)
        t_count = nucleotide_counts.get('T', 0)
        g_count = nucleotide_counts.get('G', 0)
        c_count = nucleotide_counts.get('C', 0)
        print(f"{gene_id}\t{a_count}\t{t_count}\t{g_count}\t{c_count}")

if __name__ == "__main__":
    main()
