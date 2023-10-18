#! usr/bin/env python3

import sys
import math

iterate_this = [101,2,15,22,95,33,2,27,72,15,52]
iterate_this = sorted(iterate_this)
iterated = iter(iterate_this)

evens_sum  = 0
odds_sum = 0

for i in iterated:
 #print(i)
  if i % 2 == 0:
    evens_sum = evens_sum + i
  else:
    odds_sum = odds_sum + i

print(f"""Sum of even numbers: {evens_sum}
Sum of odds: {odds_sum}""") 

