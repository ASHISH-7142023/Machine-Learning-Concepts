import numpy as np
marks=[23,56,87,89,54,56,21,2,0]
arr=np.array(marks)
avg=np.mean(arr)
above_avg=arr[arr>avg]
above_avg
