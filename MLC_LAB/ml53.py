import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier,plot_tree
#simulate corelated variables using a covariance matrix
mean=[0,0]
cov=[[1.0,0.6],[0.6,1.0]]
samples=np.random.multivariate_normal(mean,cov,size=5000)
x=samples[:,0]
y=samples[:,1]
print('empirical covariance :' np.cov(x,y)[0,1])
print('empirical correlation :' np.corrcoef(x,y)[0,1])

#scatter plot
plt.figure(figsize=(6,5))
plt.scater(x[:500],y[:500],s=10,alpha=0.6)
plt.title('scatter plot of correlated variables')
plt.xlabel('X');
plt.ylabel('Y')
plt.show()
