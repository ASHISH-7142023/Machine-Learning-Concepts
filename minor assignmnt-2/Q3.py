from sklearn.utils import resample
import pandas as pd

data = pd.read_csv("/home/iter/2341019494_Ashish/ML/btissue.csv")
predictors = data.iloc[:, :-1]
bootstrap_sample = resample(predictors, n_samples=100, random_state=123)

print("botstrap sample(first 10 rows):\n",bootstrap_sample.head(10))