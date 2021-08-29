import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2,3,-1],ndmin=2)
print(v1)
print(v1.T)

M = np.random.randn(3,3)
print(M)

M = np.round(M*10)
print(M)
print(M.T)

# what happens when transpose twice?
# does tranpose work on rectangular matrices?

print("------------------")

print(M)

print("------------------")

MT = M.T
print(MT)

print("------------------")

print(MT.T)

print("------------------")

MR = np.random.randn(3,5)
print(MR)
print(MR.T)


