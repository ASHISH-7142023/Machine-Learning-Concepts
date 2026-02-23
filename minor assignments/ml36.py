#4
import pandas as pd
import numpy as np
s=pd.Series([5,np.nan,8,np.nan,12])
print(s.isnull())
print(s.ffill())
s.dropna()