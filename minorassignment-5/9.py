import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
means = [np.mean(np.random.exponential(1, 40)) for _ in range(200)]
plt.hist(means, bins=25, edgecolor='black')
plt.title("CLT Check – Means of Exp(1)")
plt.show()