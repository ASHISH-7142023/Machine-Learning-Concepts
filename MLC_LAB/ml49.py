import pandas as pd
from sklearn import datasets
from scipy.linalg import svd

iris = datasets.load_iris()
predictors = iris.data[:, 0:4]
U,s,VT = svd(predictors)
print(U,s,VT)