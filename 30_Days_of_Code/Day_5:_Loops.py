# Day 5: Loops

# Task 
# Given an integer, N, print its first 10 multiples. Each multiple N * i (where 1 <= i <= 10) should be printed on a new line in the form:
# N x i = result.

# Input Format
# A single integer, N.

# Constraints
# 2 <= N <= 20

# Output Format
# Print 10 lines of output; each line i (where 1 <= i <= 10) contains the result of N * i in the form: 
# N x i = result.

#!/bin/python

import sys


N = int(raw_input().strip())

for i in range(1, 11):
    print "{} x {} = {}".format(N, i, N * i)
