#! usr/bin/env python3

import sys
import math

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

