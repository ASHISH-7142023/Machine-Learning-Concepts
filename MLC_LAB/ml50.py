import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.utils import column_or_1d

data = pd.read_csv(r"btissue.csv")
x = data.iloc[:, 0:9]
y = column_or_1d(data['class'],warn = True)

clf = LinearDiscriminantAnalysis()
lda_fit = clf.fit(x,y)
print(lda_fit)

pred = clf.predict([[1588.000000,0.085908,-0.086323,
                      516.943603,12895.342130,25.933331,
                      141.722204,416.175649,1452.331924]])
print(pred)
