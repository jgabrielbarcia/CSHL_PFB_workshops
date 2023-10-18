#! usr/bin/env python3

import sys
import math

dna_sequence = "GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG"

dna_sequence_upper = dna_sequence.upper()

nucleotide_list = list()
for nucleotide in ['A','T','C','G']:
	count = dna_sequence_upper.count(nucleotide)
	nucleotide_list.append(count) 

#List comprehension below
#nucleotides_list = [dna_sequence_upper.count(x) for x in ['A','T','C','G']]
#print(nucleotides_list)

dna_sequence2 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

dna_sequence2_U = dna_sequence2.replace('T','U')

dna_sequence_AT = dna_sequence_upper.count('A') + dna_sequence_upper.count('T')
AT_content = dna_sequence_AT/len(dna_sequence_upper)*100

dna_sequence_GC = dna_sequence_upper.count('G') + dna_sequence_upper.count('C')
GC_content = dna_sequence_GC/len(dna_sequence_upper)*100

dna_substring = dna_sequence_upper[99:199] 
dna_substring_GC = dna_substring.count('G')

print("\nThere are",nucleotide_list[0],"adenosines,",nucleotide_list[1],"thymines,",nucleotide_list[2],"cysteines","and",nucleotide_list[3],"guanines in the first sequence")
print("\nHere is sequence 2 in mRNA format, i.e., with uridine instead of thymine:",dna_sequence2_U)
print("\nThe AT content of the DNA sequence is:",AT_content,"%")
print("\nThe GC content of the DNA sequence is:",GC_content,"%")
print("\nThe substring from nucletide 100 to nucleotide 200 is:",dna_substring)
print("\nThe substring has",dna_substring_GC,"GCs")