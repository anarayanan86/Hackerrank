# Day 9: Recursion

# Task 
# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format
# A single integer, N (the argument to pass to factorial).

# Constraints
# 2 <= N <= 12
# Your submission must contain a recursive function named factorial.

# Output Format
# Print a single integer denoting N!.

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

print factorial(N)
