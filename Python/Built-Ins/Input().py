# Input()

# This challenge is only for Python 2.

# input()
# In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

# Code
# >>> input()  
# 1+2
# 3
# >>> company = 'HackerRank'
# >>> website = 'www.hackerrank.com'
# >>> input()
# 'The company name: '+company+' and website: '+website
# 'The company name: HackerRank and website: www.hackerrank.com'

# Task
# You are given a polynomial P of a single indeterminate (or variable), x. 
# You are also given the values of x and k. Your task is to verify if P(x) = k.

# Constraints 
# All coefficients of polynomial P are integers. 
# x and y are also integers.

# Input Format
# The first line contains the space separated values of x and k. 
# The second line contains the polynomial P.

# Output Format
# Print True if P(x) = k. Otherwise, print False.

# Sample Input
# 1 4
# x**3 + x**2 + x + 1

# Sample Output
# True

# Explanation
# P(1) = 1^3 + 1^2 + 1 + 1 = 4 = k
# Hence, the output is True.


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input().split()
x = int(a[0])
print input() == int(a[1])
