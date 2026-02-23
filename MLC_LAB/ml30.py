import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.figure()
plt.hist(data,bins=20)
plt.xlabel("value")
plt.ylabel("frquency")
plt.title("histogram")
plt.grid(True)
plt.show()