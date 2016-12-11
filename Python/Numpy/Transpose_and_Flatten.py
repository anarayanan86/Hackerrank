# Transpose

# We can generate the transposition of an array using the tool numpy.transpose. 
# It will not affect the original array, but it will create a new array.

# Flatten

# The tool flatten creates a copy of the input array flattened to one dimension.

# Task
# You are given a N X M integer array matrix with space separated elements (N = rows and M = columns). 
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M. 
# The next N lines contains the space separated elements of M columns.

# Output Format
# First, print the transpose array and then print the flatten.


import numpy

a = raw_input().split(' ')
b = tuple(map(int, a))

c = []
for i in range(b[0]):
    c.append(raw_input().split(' '))
    
c = numpy.array(c, int)
print numpy.transpose(c)
print c.flatten()
