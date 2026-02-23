import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
samples2 = np.random.uniform(-3, 3, 8000)
plt.hist(samples2, bins=30, edgecolor='black')
plt.title("Uniform(-3,3) Histogram")
plt.show()