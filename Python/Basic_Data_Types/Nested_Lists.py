# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())

students = []
for i in range(2*N):
    students.append(raw_input().split())
grades = {}
for j in range(0, len(students), 2):
    grades[students[j][0]] = float(students[j + 1][0])
result = []
num_to_match = sorted(set(grades.values()))[1]
for pupil in grades.keys():
    if grades[pupil] == num_to_match:
        result.append(pupil)
for k in sorted(result):
    print k
