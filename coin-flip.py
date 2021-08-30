import numpy as np

# create func that flips a coin N times and report average
x = 5000
def coin_flip(n):
    N = np.mean(np.random.randn(n)>0)
    print(str(n) + ' coin flips had ' + str(100*N) + '% heads.')

print(coin_flip(x))