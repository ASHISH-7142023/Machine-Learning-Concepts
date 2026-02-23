import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
#comments

iris = datasets.load_iris()
predictors = iris.data[:,0:4]
target = iris.target
predictors = StandardScaler().fit_transform(predictors)
pca = PCA(n_components=2)
princomp = pca.fit_transform(predictors)
princomp_ds = pd.DataFrame(data=princomp,columns=['PC 1','PC 2'])
print(princomp_ds)


target_ds = pd.DataFrame(data=target.reshape(-1,1),columns=['class'])
print(target_ds)

data_mod = pd.concat([princomp_ds.reset_index(drop=True),target_ds],axis=1)
fig = plt.figure(figsize=(0,0))
pca_plot = fig.add_subplot(1,1,1)
pca_plot.set_xlabel('PC 1')
pca_plot.set_ylabel('PC 2')
pca_plot.set_title('PCA(2 components)',fontsize=20)

colors = ['r','y','b']
classes=[0,1,2]
labels=['setosa','versicolor','viriginca']

for class_value, color , label in zip (classes,colors,labels):
    indices = data_mod['class'] == class_value
    pca_plot.scatter(data_mod.loc[indices,'PC 1'],
                     data_mod.loc[indices,'PC 2'],
                     c = color,
                     s = 50,
                     label = label
                     )
pca_plot.legend()
plt.show()

