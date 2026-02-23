#3
import pandas as pd
import numpy as np
arr=np.random.randint(1,101,size=10)
s=pd.Series(arr)
print(s)
print("max: ",s.max())
print("min: ",s.min())
print("mean: ",s.mean())
squared=s.apply(lambda x: x**2)
print("squared series:\n",squared)