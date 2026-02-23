import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
samples7 = np.random.poisson(4, 5000)
counts = {k: np.sum(samples7 == k) for k in range(11)}
print("7. Frequency table:", counts)