# Set .union() Operation

# .union()
# The .union() operator returns the union of a set and the set of elements in an iterable. 
# Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
# Set is immutable to the .union() operation (or | operation).

# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English,
# some have subscribed to only French and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the
# French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at
# least one newspaper.

# Input Format
# The first line contains an integer, n, the number of students who have subscribed to the English newspaper. 
# The second line contains n space separated roll numbers of those students. 
# The third line contains b, the number of students who have subscribed to the French newspaper. 
# The fourth line contains b space separated roll numbers of those students.

# Constraints
# 0 < Total number of students in college < 1000

# Output Format
# Output the total number of students who have at least one subscription.


# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_num = int(raw_input())
eng_list = raw_input().split()
eng_set = set(map(int, eng_list))
fren_num = int(raw_input())
fren_list = raw_input().split()
fren_set = set(map(int, fren_list))

print len(eng_set.union(fren_set))
