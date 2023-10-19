#! usr/bin/env python3

import sys
import math

with open("Python_06.txt","r") as hw_file:
  for line in hw_file:
    line = line.rstrip()
    line = line.upper()
    print(line)

with open("Python_06.txt","r") as hw_read_file, open("Python_06_uc.txt","w") as hw_write_file:
  for line in hw_read_file:
    line = line.rstrip()
    line = line.upper()
    hw_write_file.write(f"{line}\n")

print("Wrote 'Python_06_uc.txt'")

