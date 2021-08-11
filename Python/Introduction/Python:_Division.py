# Python: Division

# Task 
# Read two integers and print two lines. The first line should contain integer division, a // b. The second line should contain float
# division, a / b.

# You don't need to perform any rounding or formatting operations.

# Input Format 
# The first line contains the first integer, a. The second line contains the second integer, b.

# Output Format 
# Print the two lines as described above.

# Enter your code here. Read input from STDIN. Print output to STDOUT
# We have to make raw_input a variable to run the code or it says that raw_input is not defined so just run your code once before submitting
#raw_input = input
# if we not use raw_input then also we can use input and make the code run and make your code smaller
#a = int(raw_input())
#b = int(raw_input())
a = int(input())
b = int(input())
print(a // b)
print(a / b)
# If we use '//' sign it will not make the output come in decimal or float 
# I have commented the code which you can use if you want but I will recommend you to make your code smaller and more easy to write 
