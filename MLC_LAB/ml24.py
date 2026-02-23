import pandas as pd
import numpy as np
arr=np.array([10,15,18,22,55,77])
s=pd.Series(arr)
print(s)
print(s.loc[:2])
print(s.loc[3:4])
print(s.loc[2:3])
