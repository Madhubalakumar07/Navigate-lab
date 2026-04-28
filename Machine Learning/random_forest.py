import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
# Load dataset
data = load_digits()
x = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)
# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# Train the Random Forest Classifier
model = RandomForestClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(f"Predictions: {predictions}")
score = model.score(x_test, y_test)
print(f"Model Accuracy: {score:.2f}")