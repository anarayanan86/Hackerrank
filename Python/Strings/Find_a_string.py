# Find a string

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given
# string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Constraints
# 1 <= len(string) <= 200 
# Each character in the string is an ascii character.

# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Enter your code here. Read input from STDIN. Print output to STDOUT
string = raw_input()
substring = raw_input()

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1
print count
