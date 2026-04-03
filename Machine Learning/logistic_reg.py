import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#Load dataset
data = pd.read_csv(r"D:\Navigate lab\Datasets\HR_comma_sep.csv")
print(data.head())
#Initial analysis
left = data[data['left'] == 1]
stayed = data[data['left'] == 0]
print(left.shape, stayed.shape)
print(data.groupby('left').mean(numeric_only=True))
#Visualization
fig, axes = plt.subplots(2, 1, figsize=(12, 5))
sns.countplot(x='salary', hue='left', data=data, ax=axes[0])
sns.countplot(x='Department', hue='left', data=data, ax=axes[1])
plt.show()
#Prepare data for modeling
inde = data[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
print(inde.head())
dummy = pd.get_dummies(inde['salary'], drop_first=True)
salary_dummy = pd.concat([inde, dummy], axis='columns')
salary_dummy.drop('salary', axis='columns', inplace=True)
print(salary_dummy.head())
X = salary_dummy
y = data['left']
#Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Predicted values: {y_pred}")
#Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")