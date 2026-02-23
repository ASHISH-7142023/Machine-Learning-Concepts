import numpy as np
M= np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print("M[2,3]=",M[2,3])
print("row 0: ",M[0])
print("col 2: ",M[:,2])
print("submatrix(rows 0..1,cols 1...3):\n",M[0:2,1:4])