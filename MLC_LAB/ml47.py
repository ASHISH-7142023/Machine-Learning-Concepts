import pandas as pd
from sklearn import preprocessing
marks_science=[78,56,87,91,45,62]
marks_maths=[75,62,90,95,42,57]
grade=['B','C','A','A','D','B']
data=pd.DataFrame({
    'science marks': marks_science
    'total grade' : grade
})
print(data)
le=preprocessing.LabelEncoder()
le.fit(data['total grade'])
data['total grade']=le.transform(data['total grade'])
print(data)

target=data['total grade'].replace(['A','B','C','D'],[0,1,2,3])
predictors=data.iloc[:, 0:2]
data_mod=pd.concat([predictors.reset_index(drop=True),target],axis=1)