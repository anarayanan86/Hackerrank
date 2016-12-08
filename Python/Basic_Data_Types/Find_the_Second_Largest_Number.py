# Find the Second Largest Number

# You are given N numbers. Store them in a list and find the second largest number.

# Input Format 
# The first line contains N. The second line contains an array A[] of N integers each separated by a space.

# Constraints
# 2 <= N <= 10
# -100 <= A[i] <= 100

# Output Format 
# Output the value of the second largest number.


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
O = raw_input().split(' ')
P = list(map(int, O))
Q = set(P)
R = sorted(list(Q))
print R[-2]
