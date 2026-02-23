import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
samples4 = np.random.normal(12, 3, 2000)
sim_prob = np.mean(samples4 > 15)
theo_prob = 1 - norm.cdf(15, loc=12, scale=3)
print("4. Simulated P(X>15):", sim_prob)
print("   Theoretical P(X>15):", theo_prob)