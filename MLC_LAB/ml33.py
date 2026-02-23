import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
d1=np.random.normal(100,20,80)
d2=np.random.normal(90,30,60)
d3=np.random.normal(60,40,70)
d4=np.random.normal(50,10,40)
plt.figure()
plt.boxplot([d1,d2,d3,d4])
plt.xlabel("group")
plt.ylabel("value")
plt.title("box plot")
plt.grid(True)
plt.show()