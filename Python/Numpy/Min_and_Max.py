# Min and Max

# Task
# You are given a 2-D array with dimensions NxM. 
# Your task is to perform the min function over axis 1 and then find the max of that.

# Input Format
# The first line of input contains the space separated values of N and M. 
# The next N lines contains M space separated integers.

# Output Format
# Compute the min along axis 1 and then print the max of that result.


import numpy

N_M = map(int, raw_input().split())
a = numpy.array([map(int, raw_input().split()) for i in range(N_M[0])])
print numpy.max(numpy.min(a, axis = 1))
