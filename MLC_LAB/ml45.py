import pandas as pd
room_length=[18,20,10,12,18,11]
room_breadth=[20,29,10,11,19,10]
room_type=['Big','Big','Normal','Normal','Big','Normal']
data=pd.DataFrame({
    'length':room_length, 
    'breadth':room_breadth,
    'type':room_type
})
print(data)
data['area']=data['length']*data['breadth']
print(data)