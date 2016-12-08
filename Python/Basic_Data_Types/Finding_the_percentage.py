# Finding the percentage

# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The
# marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save
# the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that
# student, correct to two decimal places.

# Input Format
# The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student
# separated by a space. The final line contains the name of a particular student previously listed.

# Constraints
# 2 <= N <= 10
# 0 <= Marks <= 100

# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
results = {}
for i in range(N):
    a = raw_input().split(' ')
    results[a[0]] = [float(x) for x in a[1:]]
student = raw_input()
print "%.2f" %(sum(results[student])/len(results[student]))
