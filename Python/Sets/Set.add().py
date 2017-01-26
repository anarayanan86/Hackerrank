# Set.add()

# If we want to add a single element to an existing set, we can use the .add() operation. 
# It adds the element to the set and returns 'None'.

# Example
# >>> s = set('HackerRank')
# >>> s.add('H')
# >>> print s
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# >>> print s.add('HackerRank')
# None
# >>> print s
# set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

# Task
# Apply your knowledge of the .add() operation to help your friend Rupal.
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She
# asked for your help. You pick the stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.

# Input Format
# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from. 

# Constraints
# 0 < N < 1000

# Output Format
# Output the total number of distinct country stamps on a single line.

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
s = set(raw_input() for i in range(N))
    
print len(s)
