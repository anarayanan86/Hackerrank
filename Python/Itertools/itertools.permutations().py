# itertools.permutations()

# itertools.permutations(iterable[, r])
# This tool returns successive r length permutations of elements in an iterable.
# If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced
# in a sorted order.

# Task
# You are given a string S. 
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# Input Format
# A single line containing the space separated string S and the integer value k.

# Constraints
# 0 < k <= len(S) 
# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string S on separate lines.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S = raw_input().split()

for i in sorted(permutations(S[0], int(S[1]))):
    print ''.join(i)
