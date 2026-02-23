import pandas as pd
data = pd.read_csv("btissue.csv")
data.head()
from sklearn.model_selection import train_test_split
data.shape
data_train,data_test=train_test_split(data, test_size=0.3,random_state=123)
len(data_train)
len(data_test)
train_test_split(data, test_size = 0.3, random_state=123)
from sklearn.model_selection import KFold
kf = KFold(n_splits=10, shuffle=True, random_state=123)