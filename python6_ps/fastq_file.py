#! usr/bin/env python3

import sys
import math

character_count = 0 
line_count = 0

with open("Python_06.fastq","r") as hw_file:
  for line in hw_file:
    line_count += 1
    character_count += len(line)

avg = int(character_count / line_count)

print("Total Lines", line_count + 1, "\nTotal characters:", character_count, "\nAverage chars per line", avg)  

