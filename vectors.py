import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# vec2d = np.array([1,2]) 
# s1 = 2
# s2 = .5
# s3 = -1

# plt.plot([0,vec2d[0]], [0, vec2d[1]], 'bs--')
# plt.plot([0,s1*vec2d[0]], [0, s1*vec2d[1]], 'ro-', label='v*s1')
# plt.plot([0,s2*vec2d[0]], [0, s2*vec2d[1]], 'rp-', label='v*s2')
# plt.plot([0,s3*vec2d[0]], [0, s3*vec2d[1]], 'g*-', label='v*s3')

# plt.axis('square')
# plt.xlim([-4,4])
# plt.ylim([-4,4])

avec1 = [4,6]
avec2 = [9,10]
plt.plot([0, avec1[0]], [0, avec1[1]], 'bs--', label='vec1')
plt.plot([0,avec2[0]], [0, avec2[1]], 'rp-', label='vec2')

plt.plot([0,avec1[0]+avec2[0]], [0, avec1[1]+avec2[1]], '--', label='v1+v2')
plt.plot([0,avec1[0]-avec2[0]], [0, avec1[1]-avec2[1]], '--', label='v1-v2')
plt.plot([0,avec1[0]*4+avec2[0]/2], [0, avec1[1]*4+avec2[1]/2], '--', label='v1*4+v2/2')

plt.grid()
plt.legend()
plt.show()
