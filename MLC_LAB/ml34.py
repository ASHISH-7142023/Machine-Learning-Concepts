import pandas as pd
import numpy as np
url=r"/home/iter/Downloads/auto+mpg/auto-mpg.data"

columns=[
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
    "origin",
    "car_name"

]
df = pd.read_csv(url,delim_whitespace=True,names=columns,na_values='?')
print(df.head())
df.to_csv("auto-mpg.csv",index=False)
print("done")