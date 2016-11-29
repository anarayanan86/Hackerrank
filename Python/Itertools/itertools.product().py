# itertools.product()

# itertools.product()

# This tool computes the cartesian product of input iterables. 
# It is equivalent to nested for-loops. 
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# Task
# You are given a two lists A and B. Your task is to compute their cartesian product X.

# Example
# A = [1, 2]
# B = [3, 4]
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

# Input Format
# The first line contains the space separated elements of list A. 
# The second line contains the space separated elements of list B.

# Both lists have no duplicate integer elements.

# Constraints
# 0 < A < 30
# 0 < B < 30
 
# Output Format
# Output the space separated tuples of the cartesian product.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = raw_input().split()
A = list(map(int, A))
B = raw_input().split()
B = list(map(int, B))

for i in product(A, B):
    print i,
