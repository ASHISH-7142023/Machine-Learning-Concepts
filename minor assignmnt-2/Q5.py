import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

data=pd.read_csv('/home/iter/2341019494_Ashish/MLC/minor assignmnt-2/auto_mpg.csv')
print(data)
data=data.dropna(axis=0,how='any')
print(data)
X=data.iloc[:, 1:0]
Y=data.iloc[:, 0]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=123)
model=LinearRegression().fit(X_train,Y_train)
Y_pred=model.predict(X_test)
print("mean squared error : ",mean_squared_error(Y_test,Y_pred))