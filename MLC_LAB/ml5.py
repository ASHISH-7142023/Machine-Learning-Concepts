#ravel-> 1-D view
import numpy as np
y= np.array([[1,2,3]],dtype='float32')
print (y)
print(y.shape)
print(y[0, 1])
y1D=y.ravel()
print(y1D)
print(y1D.shape)
print(y1D[1])
#reshape to 1D length 3
y1Dv2=y.reshape(3)
print(y1Dv2)
print(y1Dv2.shape)
print(y1Dv2[1])
