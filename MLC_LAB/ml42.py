from sklearn.model_selection import train_test_split
predictors_train, predictors_test, target_train, target_test = train_test_split(predictors, target, test_size=0.3, random_state=123)
predictors_train.head()
