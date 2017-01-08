# Polynomials

# poly
# The poly tool returns the coefficients of a polynomial with the given sequence of roots.
# print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

# roots
# The roots tool returns the roots of a polynomial with the given coefficients.
# print numpy.roots([1, 0, -1])           #Output : [-1.  1.]

# polyint
# The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
# print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]

# polyder
# The polyder tool returns the derivative of the specified order of a polynomial.
# print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]

# polyval
# The polyval tool evaluates the polynomial at specific value.
# print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34

# polyfit
# The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
# print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

# The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of
# polynomial coefficients, respectively.

# Task
# You are given the coefficients of a polynomial P. 
# Your task is to find the value of P at point x.

# Input Format
# The first line contains the space separated value of the coefficients in P. 
# The second line contains the value of x.

# Output Format
# Print the desired value.

# Sample Input
# 1.1 2 3
# 0

# Sample Output
# 3.0


import numpy

P = map(float, raw_input().split())
print numpy.polyval(P, int(raw_input()))
