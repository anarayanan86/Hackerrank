# Sum and Prod

# Task
# You are given a 2-D array with dimensions N X M. 
# Your task is to perform the sum tool over axis 0 and then find the product of that result.

# Input Format
# The first line of input contains space separated values of N and M. 
# The next N lines contains M space separated integers.

# Output Format
# Compute the sum along axis 0. Then, print the product of that sum.


import numpy

N_M = map(int, raw_input().split())
a = numpy.array([map(int, raw_input().split()) for i in range(N_M[0])])
print numpy.prod(numpy.sum(a, axis = 0))
