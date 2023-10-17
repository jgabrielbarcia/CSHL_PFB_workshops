#!/usr/bin/env python3

import sys
import math

number_input = sys.argv[1]

message_list = []

if int(number_input) > 0:
  message_list.append("is positive")
  if int(number_input) > 50:
    message_list.append("greater than 50")
    if int(number_input) % 3 == 0:
      message_list.append("divisible by 3")
  elif int(number_input) < 50:
    message_list.append("smaller than 50")
    if int(number_input) % 2 == 0:
      message_list.append("even")
elif int(number_input) == 0:
  message_list.append("is exactly zero")
else:
  message_list.append("is smaller than zero")

if len(message_list) == 2:
  print(number_input, " and ".join(message_list))
elif len(message_list) > 2:
  print(number_input, ", ".join(message_list[0:-1]),"and",message_list[-1])
else:
  print(number_input, " ".join(message_list))


