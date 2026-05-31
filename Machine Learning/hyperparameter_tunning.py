import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv(r"D:\Navigate lab\Datasets\diabetes.csv")
print(df.head())

# Split data into features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model and hyperparameters for tuning
model = RandomForestClassifier()
param_grid = {
    'n_estimators': [100, 150, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

# Perform hyperparameter tuning using GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best model and evaluate it on the test set
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test, y_test)
print(f'Best Hyperparameters: {grid_search.best_params_}')
print(f'Test Set Accuracy: {test_score:.2f}')