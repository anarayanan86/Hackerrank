# Incorrect Regex

# You are given a string S. 
# Your task is to find out whether S is a valid regex or not.

# Input Format
# The first line contains integer T, the number of test cases. 
# The next T lines contains the string S.

# Constraints
# 0 < T < 100

# Output Format
# Print "True" or "False" for each test case without quotes.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(raw_input())
for i in range(T):
    try:
        re.compile(raw_input())
        print True
    except:
        print False
