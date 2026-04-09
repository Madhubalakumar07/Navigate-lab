import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
data = load_digits()
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
score = model.score(x_test, y_test)
print(f"Model Accuracy: {score:.2f}")
