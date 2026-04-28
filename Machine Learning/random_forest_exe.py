import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
# Load dataset
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data", header=None)
# Define feature columns and target column
feature_cols = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
target_col = ['class']
df.columns = feature_cols + target_col
print(df.head())
# Encode categorical features
oe = OrdinalEncoder()
df[feature_cols] = oe.fit_transform(df[feature_cols])
df[target_col] = oe.fit_transform(df[target_col])
print(df.head())
# Split data into features and target
x = df[feature_cols]
y = df[target_col]
# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
model = RandomForestClassifier()
model.fit(x_train, y_train)
# Predict on the test set
y_pred = model.predict(x_test)
print("Predictions:", y_pred)
# Evaluate the model
acc = model.score(x_test, y_test)
print("Accuracy:", acc)