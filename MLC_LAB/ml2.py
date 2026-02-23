import numpy as np
b=np.array([1 , 2 , 3])
print("b.dtype: ",b.dtype)
b_float=b.astype('float64')
print("casted: ",b_float,b_float.dtype)
s=np.array(['3.14','2.71','1.00'])
print("as float: ",s.astype('float32'))