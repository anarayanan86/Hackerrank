# Introduction to Sets

# A set is an unordered collection of elements without duplicate entries. 
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# Basically, sets are used for membership testing and eliminating duplicate entries. 
# let's get it through the example
# >> print set()
# set([])

# >>> print set('HackerRank')
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

# >>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
# set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

# >>> print set((1,2,3,4,5,5))
# set([1, 2, 3, 4, 5])

# >>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
# set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
# set(['Hacker', 'Rank'])

# >>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
# set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])

# Task
# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the
# plants with distinct heights in her greenhouse.

# Formula used:
# Average = Sum of Distinct Heights / Total Number of Distinct Heights

# Input Format
# The first line contains the integer, N, the total number of plants.
# The second line contains the N space separated heights of the plants.

# Constraints
# 0 < N <= 100

# Output Format
# Output the average height value on a single line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
O = set(map(int, raw_input().split()))
print float(sum(O))/len(O)
