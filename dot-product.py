# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# v1 = np.array([4,5,6,2])
# v2 = np.array([-4,3,0])

# np.dot(v1,v2)
# ValueError: shapes (4,) and (3,) not aligned: 4 (dim 0) != 3 (dim 0)

# v1 = np.array([5,6,2])
# v2 = np.array([3,0,5])

# print(np.dot(v1,v2)) # 25

# v3 = np.array([-4,3,1])

# print(np.dot(v2,v3)) # -7

# v4 = np.array([0,0,0]) # zeros vector

# print(np.dot(v4,v3)) # 0

# v3 = np.array([-4,3,1])
# v5 = np.array([2,3,-1])

# print(np.dot(v3,v5)) # 0 -> 2*-4 / 3*3 / -1*1 -> -8+9-1 -> 0
#   v3 is arthogonal to v5
#   *               
#   *           
#   *        
#   *            
#   * * * * * *   

# create 3 2D vectors
# 2 should be arthogonal
# But neither orthogonal to the third

avec1 = np.array([3,-3])
avec2 = np.array([-3,-3])
avec3 = np.array([1,4])

print(np.dot(avec1,avec2)) # 0

plt.plot([0,avec1[0]],[0,avec1[1]],'-', label='avec1')
plt.plot([0,avec2[0]],[0,avec2[1]],'--', label='avec2')
plt.plot([0,avec3[0]],[0,avec3[1]],'b-', label='avec3')

plt.axis('square')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.grid()
plt.legend()
plt.show()