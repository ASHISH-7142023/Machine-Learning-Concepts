# prior probability base ---
# tumor is malignant in only 0.55 % of population
# P(Malignant)=0.005
# P(Not Malignant)=0.995



# test accuracy (true +ve) ---
import pandas as pd
import numpy as np
from sklearn.model_selection import  train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
data=pd.read_csv("apndcts.csv")
print (data)
pred=data.iloc[:0:7]
target=data.iloc[:,7]
pred_train,pred_test,target_train,target_test = train_test_split(pred,target,test_size=0.8,random_state=123)
gnb=GaussianNB()
 











