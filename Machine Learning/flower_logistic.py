import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
# Load the Iris dataset
data = load_iris()
print(dir(data))
X = data.data
print(X)
y = data.target
print(y)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(x_train,y_train)
print(model.predict([[6.8, 3.0, 5.5, 2.1]]))
score = model.score(x_test,y_test)
print(score)