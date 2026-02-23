#numpy array of
import numpy as np
ar= np.random.randint(0,10,size=10)
ar2= np.random.randint(0,10,size=10)
print(ar)
print(ar2)
count=0
for i in range (10):
    if ar[i]>ar2[i]:
        count=count+1
count