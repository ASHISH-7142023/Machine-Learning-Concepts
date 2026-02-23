import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import factorial,sqrt,pi
np.random.seed(42)

#bernoulli discrete sample
p=0.3
n_samples=10000
bern=np.binomial(1,p,size=n_samples)
print('bernoulli sample mean(approx p):',bern_mean())
print('bernoulli sample var(approx p(1-p)):',bern_var())

#normal continous sample
mu,sigma=2.0,1.5
norm_samples=np.random.normal(mu,sigma,size=n_samples)
print('\n normal sample mean(approx mu):',norm_samples.mean())
print('\n normal sample var(approx sigma^2):',norm_samples.var())

#ploty pdfs and pmfs
fig,axes=plt.subplots(1,2,figsize=(10,4))

#bernoulli PMF
vals,counts = np.unique(bern,return_counts=True)
axes[0].bar(vals,counts/len(bern))
axes[0].set_title('bernoulli pmf(empirical)')
axes[0].set_xlabel('value'))
axes[0].set_ylabel('probability')

#normal pdf (empirical histogram + theoritical pdf)
axes[1].hist(norm_samples,bin=40,density=True)
x=np.linspace(mu-4*sigma,mu+4*sigma,200)
axes[1].plot(x,stats.pdf(x,norm,sigma))
axes[1].set_title('normal pdf (empirical+theoritical)')
plt.tight_layout()
plt.show()
