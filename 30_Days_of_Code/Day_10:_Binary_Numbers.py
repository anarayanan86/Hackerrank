# Day 10: Binary Numbers

# Task 
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of
# consecutive 1's in n's binary representation.

# Input Format
# A single integer, n.

# Constraints
# 1 <= n <= 10^6

# Output Format
# Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

#!/bin/python

import sys


n = int(raw_input().strip())
a = str(bin(n)[2:])

b = a.split("0")
max_length = 0
for i in b:
    if len(i) > max_length:
        max_length = len(i)
        
print max_length
