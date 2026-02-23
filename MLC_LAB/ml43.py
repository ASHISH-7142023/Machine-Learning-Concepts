import numpy as np
import pandas as pd
from sklearn .cluster import KMeans
from sklearn.metrics.cluster import v_measure_score
data = pd.read_csv("/home/iter/2341019494_Ashish/Dataset_spine.csv")

data.head()

np.shape(data)

data_woc = data.iloc[:,0:12]
data_woc

data_class = data.iloc[:,12]
data_class

f1=data_woc['Col1'].values
#f1

f2=data_woc['Col5'].values
f3=data_woc['Col9'].values

X=np.array(list(zip(f1,f2,f3)))
X

kmeans = KMeans(n_clusters=2,random_state=123)

model = kmeans.fit(X)

cluster_labels = kmeans.product(X)
v = v_measure_score(cluster_labels,data_class)
print(v)

from sklearn.metrics import silhouette_score
sil=silhouette_score(X, cluster_labels,metric='euclidean')
print(sil)





