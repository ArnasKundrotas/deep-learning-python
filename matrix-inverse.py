import numpy as np
import matplotlib.pyplot as plt

# matrix division does not exist
# 2/3 = 2*3**-1
# matrix A/B = A*B**-1
# Ax=b -> A**-1*Ax=A**-1*b -> Ix=A**-1b -> x=A**-1*b

A = np.random.randn(4,4)
Ainv = np.linalg.inv(A)

AinvA = A@Ainv

print(A)
print(Ainv)
print(AinvA)

# fig,ax = plt.subplots(1,3,figsize=(6,5))

# ax[0].imshow(A)
# ax[0].set_title('A')
# ax[1].imshow(Ainv)
# ax[1].set_title('A$^{-1}$')
# ax[2].imshow(AinvA)
# ax[2].set_title('A$^{-1}$A')

plt.show()

# create vector 3D, create diagonal matrix from the vector and compute inverse
# cerate a 2x3 matrix, try to compute its inverse
vec = np.array([1,2,3])
m = 3
M = np.tile(vec,(m,1))
MI = np.eye(3) 
print("-------------")
print(M)
print(MI)
Md = M*MI
print(Md)
print(np.linalg.inv(Md))
print("-------------")
M2 = np.random.randn(2,3)
print(np.linalg.inv(M2)) # <-- error array must be square
