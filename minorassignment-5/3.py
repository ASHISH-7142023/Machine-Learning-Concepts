import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson
samples3 = np.random.normal(10, 2, 3000)
print("3. Sample mean:", samples3.mean())
print("   Sample variance:", samples3.var())