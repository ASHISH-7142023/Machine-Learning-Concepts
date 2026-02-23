import pandas as pd
s1= pd.Series[1,2,3,4,5], index = ['a','b','c','d','e']
s2= pd.Series[10,20,30,40,50], index = ['a','b','c','d','e']
s3= pd.Series[5,14,23,32], index = ['a','b','c','d']
print('to add Series1 and Series2')
print('-------------------')
print(s1 + s2)

print('to add Series2 & Series3')