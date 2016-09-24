# Objective 
# Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and
# an instructional video!

# Context 
# Given a 6 x 6 2D Array, A:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task 
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the
# inclusive range of -9 to 9.

# Constraints
# -9 <= A[i][j] <= 9
# 0 <= i,j <= 5

# Output Format
# Print the largest (maximum) hourglass sum found in A.

#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
   
res = []

for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print max(res)
