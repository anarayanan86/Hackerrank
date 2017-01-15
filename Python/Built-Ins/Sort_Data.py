# Sort Data

# You are given data in a tabular format. The data contains N rows, and each row contains M space separated elements.
# You can imagine the M items to be different attributes, (like height, weight, energy, etc.) and each of the N rows as an instance or a
# sample.
# Your task is to sort the table on the Kth attribute and print the final resulting table.
# Note: If two attributes are the same for different rows, print the row that appeared first in the input.

# Input Format
# The first line contains N and M separated by a space. 
# The next N lines each contain M elements. 
# The last line contains K.

# Constraints
# 1 <= N, M <= 1000
# 0 <= K < M
# Each element <= 1000

# Output Format
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

# Sample Input
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# Sample Output
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12

# Explanation
# The table is sorted on the second attribute shown as K = 1 because it's 0-indexed.


# Enter your code here. Read input from STDIN. Print output to STDOUT
NM = map(int, raw_input().split())
a = [map(int, raw_input().split()) for i in range(NM[0])]
K = int(raw_input())
a.sort(key = lambda x: x[K])
for i in a:
    for j in i:
        print j,
    print
