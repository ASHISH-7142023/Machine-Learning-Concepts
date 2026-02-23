import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
samples6 = np.random.exponential(1/1.2, 7000)
x = np.linspace(0, samples6.max(), 200)
plt.hist(samples6, bins=40, density=True, alpha=0.6)
plt.plot(x, 1.2 * np.exp(-1.2*x))
plt.title("Exponential(λ=1.2) Histogram + PDF")
plt.show()