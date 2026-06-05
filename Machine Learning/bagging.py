import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
data = pd.read_csv(r"D:\Navigate lab\Datasets\heart.csv")
print(data.head())

# Prepare data
X = data.drop('HeartDisease', axis='columns')
y = data['HeartDisease']
le = LabelEncoder()
for column in X.select_dtypes(include=['object']):
    X[column] = le.fit_transform(X[column])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train in svm
svm = SVC(kernel='rbf', C=1)
scores_svm_before = cross_val_score(svm, x_train, y_train, cv=5)
print(f'SVM Cross-Validation Scores before Bagging: {scores_svm_before.mean():.4f}')
bagging_svm = BaggingClassifier(estimator = SVC(kernel='rbf', C=1), n_estimators=10, max_samples=0.8, random_state=42)
scores_bagging_svm = cross_val_score(bagging_svm, x_train, y_train, cv=5)
print(f'Bagging SVM Cross-Validation Scores: {scores_bagging_svm.mean():.4f}')

# Train in Decision Tree
dt = DecisionTreeClassifier(random_state=42)
scores_dt_before = cross_val_score(dt, x_train, y_train, cv=5)
print(f'Decision Tree Cross-Validation Scores before Bagging: {scores_dt_before.mean():.4f}')
bagging_dt = BaggingClassifier(estimator=DecisionTreeClassifier(random_state=42), n_estimators=10, max_samples=0.8, random_state=42)
scores_bagging_dt = cross_val_score(bagging_dt, x_train, y_train, cv=5)
print(f'Bagging Decision Tree Cross-Validation Scores: {scores_bagging_dt.mean():.4f}')