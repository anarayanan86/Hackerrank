# List Comprehensions

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print ans
