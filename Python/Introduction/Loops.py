# Loops

# Task 
# Read an integer N. For all non-negative integers i < N, print i**2. See the sample for details.

# Input Format
# The first and only line contains the integer, N.

# Constraints
# 1 <= N <= 20

# Output Format
# Print N lines, one corresponding to each i.

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

for i in range(N):
    print i * i
