# Inner and Outer

# inner
# The inner tool returns the inner product of two arrays.

# import numpy

# A = numpy.array([0, 1])
# B = numpy.array([3, 4])

# print numpy.inner(A, B)     #Output : 4

# outer
# The outer tool returns the outer product of two arrays.

# import numpy

# A = numpy.array([0, 1])
# B = numpy.array([3, 4])

# print numpy.outer(A, B)     #Output : [[0 0]
#                             #          [3 4]]

# Task
# You are given two arrays: A and B. 
# Your task is to compute their inner and outer product.

# Input Format
# The first line contains the space separated elements of array A. 
# The second line contains the space separated elements of array B.

# Output Format
# First, print the inner product. 
# Second, print the outer product.


import numpy

A = numpy.array(raw_input().split(), int)
B = numpy.array(raw_input().split(), int)

print numpy.inner(A, B)
print numpy.outer(A, B)
