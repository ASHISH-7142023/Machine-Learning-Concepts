import pandas as pd
age=[18,20,23,19,18,22,21]
city=['A','B','B','A','A','C','B']
data=pd.DataFrame({'age':age,'city':city})
print(data)
dummy_features=pd.get_dummies(data['city'])
data_age=pd.DataFrame(data=data,columns=['age'])
data_mod=pd.concat([data_age.reset_index(drop=True),dummy_features],axis=1)
print(data_mod)