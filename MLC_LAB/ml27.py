import pandas as pd
marks=pd.DataFrame({
    'yash': [87,89,93,87,92],
    'ashish': [87,94,51,97,96],
    'sailesh': [56,89,84,51,53],
    'subu': [78,85,45,52,66],
    'sara': [86,89,52,65,58]
},index = ['test01','test02','test03','test04','test05'])
print('all marks:')
print(marks)
print(marks.yash.test01)
print(marks.iat[0,1])
print(marks.at['test01','sara'])
print('O grade students: ')
print(marks[marks>=90])
print('\nA grade students :')
print(marks[(marks>=80)&(marks<90)])
marksTransposed = marks.T
print(marksTransposed)
#row indices
print(marks.sort_index(ascending=False)) #for test
print(marks.sort_index(axis=1)) # for names
print(marks.sort_values(by='test01',axis=1,ascending=False))
print(marks.sort_values(by='test02',axis=1,ascending=False))
print(marks.T.sort_values(by='test01',ascending=False))
print(marks.loc['test01'].sort_values(ascending=False))

