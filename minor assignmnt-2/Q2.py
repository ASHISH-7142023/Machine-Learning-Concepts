import pandas as pd
from sklearn.model_selection import KFold

data = pd.read_csv("/home/iter/2341019494_Ashish/ML/btissue.csv")

kf = KFold(n_splits=5,shuffle=True,random_state=123)
for fold, (train_index,test_index) in enumerate(kf.split(data)):
    print(f"\n Fold{fold}")
    print("train indices : ", train_index)
    print("test indices : ",test_index)
    
folds = list(kf.split(data))
train_index, test_index = folds[2]
data_train = data.iloc[train_index]
data_test = data.iloc[test_index]

print("\n---Fold3 Details---")
print("training set length : \n", len(data_train))
print("test set length : \n", len(data_test))
print("training set sample : \n", data_train.head())
print("test set sample : \n", data_test.head())


