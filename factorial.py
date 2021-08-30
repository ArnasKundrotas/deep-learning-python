import math
import numpy as np

n = 12

def factorial_our (n):
  ans = 1
  while n >=1:
    ans *= n
    n -= 1
  return ans

(factorial_our(n) == math.factorial(n))

def my_fact(n):
  return np.prod(np.arange(1,n+1))
  
print("------------------")
print(factorial_our(n))
print("------------------")
print(my_fact(n))
print("------------------")

print(factorial_our(n) == my_fact(n))

# n = 12 True
# ------------------
# 479001600
# ------------------
# 479001600
# ------------------
# True

# n = 123 False <-- overflow
# 12146304367025329675766243241881295855454217088483382315328918161829235892362167668831156960612640202170735835221294047782591091570411651472186029519906261646730733907419814952960000000000000000000000000000
# ------------------
# 0
# ------------------
# False