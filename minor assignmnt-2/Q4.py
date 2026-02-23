import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClass
from sklearn.metrics import accuracy_score,confusion_matrix

data = pd.read_csv("/home/iter/2341019494_Ashish/ML/btissue.csv")
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

x_train, x_test, y_train,y_test = train_test_split ( x,y,test_size=0.2,random_state=123)
rf = RandomForestClassifier(random_state=123)
rf.fit(x_train,y_train)

y_pred = rf.predict(x_test)

print("accuracy : ",accuracy_score(y_test,y_pred))
print("confusion matrix :\n",confusion_matrix(y_test, y_pred))