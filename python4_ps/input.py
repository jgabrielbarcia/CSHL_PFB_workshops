#! usr/bin/env python3

import sys
import math

#Write a new script that takes the start and end values from the command line (sys.argv). If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

number_input = sys.argv[1:]
i = ""

for i in number_input:
  if i == number_input[0]:
    first = int(i)
  elif i == number_input[-1]:
    last = int(i) + 1

seq = list(range(int(first),last))

for i in seq:
  if i % 2 != 0:
    print(i)

