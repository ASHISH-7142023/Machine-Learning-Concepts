import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("/home/iter/2341019494_Ashish/auto_mpg.csv")
print("shape of dataset : ",data.shape)
data_train, data_test =train_test_split(data, test_size=0.2,random_state=123)

print("\n training set:\n",data_train.head())
print("\n test set:\n",data_test.head())
print("\n length of training set:\n",len(data_train))
print("\n length of test set:\n",len(data_test))