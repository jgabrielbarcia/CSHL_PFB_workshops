#! usr/bin/env python3

import sys
import math

taxa = 'sapiens erectus neanderthalensis'

print("Print taxa:",taxa)

print("Print taxa[1]:",taxa[1])

print("Print type(taxa):",type(taxa))

print("Split taxa into individual words and print the result of the split:",taxa.split())

species = taxa.split()
print("Print species:",species)

print("Print species[1]:",species[1])

print("Print type(species):",type(species))

species_sorted = sorted(species)
print("Sort the list alphabetically and print:",species_sorted)


