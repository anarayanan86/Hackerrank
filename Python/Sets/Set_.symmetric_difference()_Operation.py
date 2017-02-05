# Set .symmetric_difference() Operation

# .symmetric_difference()
# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
# Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
# The set is immutable to the .symmetric_difference() operation (or ^ operation).

# >>> s = set("Hacker")
# >>> print s.symmetric_difference("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

# >>> print s.symmetric_difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

# >>> s ^ set("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# Task
# Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some
# have subscribed to French only, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the
# French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper
# but not both.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper. 
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper. 
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Constraints
# 0 < Total number of students in college < 1000

# Output Format
# Output total number of students who have subscriptions to the English or the French newspaper but not both.


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = raw_input().split()
b = list(map(int, b))
c = int(raw_input())
d = raw_input().split()
d = list(map(int, d))

print len(set(b).symmetric_difference(set(d)))
