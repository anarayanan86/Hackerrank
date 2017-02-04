# Set .difference() Operation

# .difference()
# The tool .difference() returns a set with all the elements from the set that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).

# >>> s = set("Hacker")
# >>> print s.difference("Rank")
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(['R', 'a', 'n', 'k'])
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', 'H', 'k'])

# >>> print s.difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'r'])

# >>> s - set("Rank")
# set(['H', 'c', 'r', 'e'])

# Task
# Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English
# newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the
# French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper. 
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper. 
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Constraints
# 0 < Total number of students in college < 1000

# Output Format
# Output the total number of students who are subscribed to the English newspaper only.


# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_num = int(raw_input())
eng_set = set(map(int, raw_input().split()))
fren_num = int(raw_input())
fren_set = set(map(int, raw_input().split()))

print len(eng_set.difference(fren_set))
