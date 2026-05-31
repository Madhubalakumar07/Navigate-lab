import pandas as pd
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import load_digits

# Load dataset
data = load_digits()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Split dataset into features and target variable
X = df.drop('target', axis=1)
y = df['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define models and their hyperparameters for tuning
models = {
    'SVC': (SVC(), {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}),   
    'RandomForest': (RandomForestClassifier(), {'n_estimators': [100, 200], 'max_depth': [None, 10]}),
    'LogisticRegression': (LogisticRegression(max_iter=1000), {'C': [0.1, 1, 10]}),
    'GaussianNB': (GaussianNB(), {}),
    'MultinomialNB': (MultinomialNB(), {}),
    'DecisionTree': (DecisionTreeClassifier(), {'max_depth': [None, 10, 20]})
}

# Perform hyperparameter tuning and evaluate models
for model_name, (model, params) in models.items():
    print(f'Tuning {model_name}...')
    grid_search = GridSearchCV(model, params, cv=5)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    score = best_model.score(X_test, y_test)
    print(f'{model_name} Best Parameters: {grid_search.best_params_}')
    print(f'{model_name} Accuracy: {score:.2f}\n')