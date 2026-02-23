import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
u = np.random.uniform(0, 8, 5000)
e = np.random.exponential(1/0.2, 5000)
plt.hist(u, bins=40, alpha=0.6, label="Uniform(0,8)")
plt.hist(e, bins=40, alpha=0.6, label="Exponential(λ=0.2)")
plt.legend()
plt.title("Uniform vs Exponential")
plt.show()