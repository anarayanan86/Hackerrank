# Eye and Identity

# identity
# The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest
# as 0. The default type of elements is float.

# import numpy
# print numpy.identity(3) #3 is for  dimension 3 X 3

# Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

# eye
# The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the
# optional parameter k. A positive k is for the upper diagonal, a negative k is for the lower, and a 0 k (default) is for the main
# diagonal.

# import numpy
# print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
# [[ 0.  1.  0.  0.  0.  0.  0.]
#  [ 0.  0.  1.  0.  0.  0.  0.]
#  [ 0.  0.  0.  1.  0.  0.  0.]
#  [ 0.  0.  0.  0.  1.  0.  0.]
#  [ 0.  0.  0.  0.  0.  1.  0.]
#  [ 0.  0.  0.  0.  0.  0.  1.]
#  [ 0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.]]

# print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.

# Task
# Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.

# Input Format
# A single line containing the space separated values of N and M. 
# N denotes the rows. 
# M denotes the columns.

# Output Format
# Print the desired NxM array.

# Sample Input
# 3 3

# Sample Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]


import numpy

N_M = map(int, raw_input().split())
print numpy.eye(N_M[0], N_M[1], k = 0)
