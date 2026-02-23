import pandas as pd
import numpy as np
arr=np.array([10,15,18,22,55,77,42])
s=pd.Series(arr)
print(s.head())
print(s.head(3))
print(s.tail())
print(s.tail(3))
