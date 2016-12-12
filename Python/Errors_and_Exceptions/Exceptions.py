# Exceptions

# Exceptions
# Errors detected during execution are called exceptions.

# Examples:

# ZeroDivisionError 
# This error is raised when the second argument of a division or modulo operation is zero.

# ValueError 
# This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

# Handling Exceptions
# The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to
# specify handlers for different exceptions.

# Output
# Error Code: integer division or modulo by zero

# Task
# You are given two values a and b. 
# Perform integer division and print a/b.

# Input Format
# The first line contains T, the number of test cases. 
# The next T lines each contain the space separated values of a and b.

# Constraints
# 0 < T < 10

# Output Format
# Print the value of a/b. 
# In the case of ZeroDivisionError or ValueError, print the error code.


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
a = []
for i in range(N):
    a.append(raw_input().split())
for j in range(len(a)):
    try:
        print int(a[j][0])//int(a[j][1])
    except ZeroDivisionError as e:
        print "Error Code:", e
    except ValueError as f:
        print "Error Code:", f
