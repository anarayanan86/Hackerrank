# Hackerrank 30 days of code
# Day 1: Data Types

# Task
# Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must declare
# variables: one of type int, one of type double, and one of type String. Then you must read 3 lines of input from stdin and initialize
# your variables. Finally, you must use the + operator to perform the following operations:

# Print the sum of i plus your int variable on a new line.
# Print the sum of d plus your double variable to a scale of one decimal place on a new line.
# Concatenate s with the string you read as input and print the result on a new line.
# Note: If you are using a language that doesn't support using + for string concatenation (e.g.: C), you can just print one variable
# immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the
# string you read as input.

# Input Format
# The first line contains an integer, i.
# The second line contains a double, d.
# The third line contains a string, s.

# Output Format
# Print the sum of both integers on the first line, the sum of both doubles (scaled to 1 decimal place) on the second line, and then the
# two concatenated strings on the third line.

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
# Don't need to explicitly declare variables in Python!

# Read and save an integer, double, and String to your variables.
a = int(raw_input())
b = float(raw_input())
c = str(raw_input())

# Print the sum of both integer variables on a new line.
print i + a

# Print the sum of the double variables on a new line.
print format(d + b, '.1f')

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print s + c


# Test Case #1 Expected output:
# 7
# 6.8
# HackerRank is my favorite platform!
