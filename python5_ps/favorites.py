#! usr/bin/env python3

import sys
import math

favorite_dict = {'Book':'Bible','Song':'Psalm','Tree':'Of life'}
print(favorite_dict['Book'])

fav_thing = 'Book'
print(favorite_dict[fav_thing])

print(favorite_dict['Tree'])

favorite_dict.update({'Organism':'Planaria'})

fav_thing = 'Organism'

print(favorite_dict[fav_thing])

for i, j in favorite_dict.items():
  print(i,": ", j, sep = "")

request = sys.argv[1]

if request in favorite_dict:
  print(favorite_dict[request])
 
