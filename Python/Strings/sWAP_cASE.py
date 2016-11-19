# sWAP cASE

# You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) <= 1000

# Output Format
# Print the modified string S.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
S = raw_input()

T = []
for i in range(len(S)):
    if S[i] in lower:
        T.append(S[i].upper())
    elif S[i] in upper:
        T.append(S[i].lower())
    else:
        T.append(S[i])
print ''.join(T)
