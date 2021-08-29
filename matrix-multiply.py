import numpy as np
import matplotlib.pyplot as plt

# A*B
#  
# A left-multiplies B
# A pre-multiplies B
# 
# B right-multiplies A
# B post-multiplies A

# M*N N*K M*K
# if M* N cols equal N *K rows -> matrices can be multiplied
# result size is M*K matrix

# 5x2 2x7 can be multplied result 5x7
# 2x5 7x2 cannot be multplied
# 5x7 5x2 cannot be multplied but can be tranposed to 7x5 and multiplied

M1 = np.random.randn(4,5) 
M2 = np.random.randn(4,5)
# 4x5 4x5
# M1*M2 cannot be multiplied
# print(np.matmul(M1,M2)) <-- error
print(np.matmul(M1,M2.T))
print(M1@M2.T)
print("--------------------")
print(np.matmul(M1,M2.T)-M1@M2.T)

# create 3x3 matrix of int
# multiply by I matrix 3x3, zeros matrix, matrix transpose

M3 = np.full((3,3),69)
M4 = np.array([[1,2,3],[3,2,1],[9,8,7]])
MI = np.eye(3)
MZ = np.zeros([3,3])
print("--------------------")
print(M3*MI)
print(M3*MZ)
print(M4*M4.T)

