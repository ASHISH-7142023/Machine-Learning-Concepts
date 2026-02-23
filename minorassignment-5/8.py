import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
samples8 = np.random.poisson(9, 3000)
plt.hist(samples8, bins=20, density=True, alpha=0.6)
x = np.linspace(min(samples8), max(samples8), 200)
plt.plot(x, norm.pdf(x, 9, 3))
plt.title("Poisson(9) vs Normal Approx.")
plt.show()