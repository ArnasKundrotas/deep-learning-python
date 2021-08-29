import numpy as np
import matplotlib.pyplot as plt

# Diagonal of the matrix
#   
# 1 0 0 0   1 0 0 0 0 0
# 0 1 0 0   0 1 0 0 0 0
# 0 0 1 0   0 0 1 0 0 0
# 0 0 0 1   0 0 0 1 0 0 
# 
# Symetric
#  1 -1  0
# -1 -2 -4
#  0 -4  5 
#
# Identity - I
# 1 0 ... 0
# 0 1 ... 0
# . .     .
# 0 0 ... 1
# Diagonal
# 1  0  0   1 0 0 0
# 0 -2  0   0 1 0 0
# 0  0  5   0 0 1 0

# Identity matrix
print(np.eye(3))

# Matrix of zeros
print(np.zeros([3,4]))

# 5x2 with all 7
print(np.full((5,2),7))

M = np.array([  [1,2,3],
                [4,5,6],
                [7,8,9]])
print(M)

# Create 3 matrices: 2x2, 2x2, 3x2
# compute scalar-matrix multiplication
# add all pairs of matrices

m1 = np.eye(2)
m2 = np.full((2,2),11)
m3 = np.array([[3,6,7],[9,8,11]])

print("------------------")
print(m1,m2,m3)

s = 4

print("------------------")
print(m1*s, m2*s,m3*s)

m4 = m1 + m2

print("------------------")
print(m4)

# adding different matrices
# direct sum
print("------------------")

m5 = m1 + m2

dsum = np.zeros(np.add(m3.shape, m5.shape))
print(dsum.shape) # 4x5 matrix
print(m3)
print(m5)

print("------------------")
dsum[:m3.shape[0],:m3.shape[1]]=m3
dsum[m3.shape[0]:,m3.shape[1]:]=m5
print(dsum)






