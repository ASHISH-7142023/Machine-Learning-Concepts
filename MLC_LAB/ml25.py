import pandas as pd
import numpy as np
arr=np.array(['a','b','c','d'])
s=pd.Series(arr,index=['first','second','third','fourth'])
print(s)
print(s.index)