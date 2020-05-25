from joblib import dump
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv('./coronaData.csv')

x = df.drop(['status'], axis=1)
y = df['status']
x = x.to_numpy()
y = y.to_numpy()

clf = DecisionTreeClassifier()
x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=0, test_size=.2)
clf.fit(x_train, y_train)
predicted = clf.predict(x_test)
print(accuracy_score(y_test, predicted))
dump(clf, "mymodel2.joblib")
