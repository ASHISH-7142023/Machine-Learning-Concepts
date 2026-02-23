import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression


print("\n --- SVM Kernel Comparison with support vectors")

#1 define training data
X = np.array([[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]])
Y = np.array([0,0,0,1,1,1])

#2

h = 0.02
X.min,X.max 




# SVM are supervised learning models primarily used for classification task
# they work on finding working planes with possible max possible matching