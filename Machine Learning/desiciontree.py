import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
# Load dataset
data = pd.read_csv(r"D:\Navigate lab\Datasets\titanic.csv")
data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked', 'SibSp'], axis=1, inplace=True)
features = data.drop('Survived', axis=1)
target = data['Survived']
features['Sex'] = features['Sex'].map({'male': 0, 'female': 1})
features['Age'] = features['Age'].fillna(features['Age'].mean())
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)
# Train the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print(f"Accuracy on test set: {model.score(X_test, y_test):.2f}")
