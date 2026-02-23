#minor assignment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(r"/home/iter/Downloads/auto+mpg/Marks.csv")
df=pd.DataFrame(data)
df.drop('Name',axis=1).plot(kind='box')
plt.title("performance analysis")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()