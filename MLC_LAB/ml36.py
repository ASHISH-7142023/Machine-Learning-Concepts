import pandas as pd
import numpy as np
data=[10,20,30,40,50]
index=['a','b','c','d','e']
s=pd.Series(data,index=index)
print(s.head(3))
print("element at index 'c' :",s['c'])