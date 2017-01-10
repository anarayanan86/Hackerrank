# Dot and Cross

# Task
# You are given two arrays A and B. Both have dimensions of NxN. 
# Your task is to compute their matrix product.

# Input Format
# The first line contains the integer N. 
# The next N lines contains N space separated integers of array A. 
# The following N lines contains N space separated integers of array B.

# Output Format
# Print the matrix multiplication of A and B.


import numpy

N = int(raw_input())
A = numpy.array([raw_input().split() for i in range(N)], int)
B = numpy.array([raw_input().split() for i in range(N)], int)
print numpy.dot(A, B)
