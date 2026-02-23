import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(0)
xs = np.random.rand(50)
ys = np.random.rand(50)
plt.figure()
plt.scatter(xs, ys, marker="*")
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatter plots(random points)")
plt.grid(True)
plt.show()