import pandas as pd
import numpy as np

# not used often in deep learning bc high dimension matrices needed
# comes up often in machine learning

# drawn from gausian distribution
# print(np.random.randn(5)) # array of 5 random number

var1 = np.random.randn(100)*5+20
var2 = np.random.randn(100)>0

labels = ['temp, C','Ice cream']

D = {labels[0]:var1,labels[1]:var2}

df = pd.DataFrame(data=D)
print(df)

print(df.head())
print(df.count())
print(df.mean())

labels1 = ['ints','squares','log']

# var3 = np.array([0,1,2,3,4,5,6,7,8,9,10])
var3 = np.array(range(11))
var4 = var3**2
var5 = var3*var3

D1 = {labels1[0]:var3, labels1[1]:var4,labels1[2]:np.log(var3)}

df1 = pd.DataFrame(D1)
print(df1)
