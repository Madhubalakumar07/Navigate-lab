from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Initialize the model
scores_logistic = cross_val_score(LogisticRegression(max_iter=200), X, y)
scores_rf = cross_val_score(RandomForestClassifier(), X, y)
scores_svm = cross_val_score(SVC(), X, y)
# Print the results
print("Logistic Regression Cross-Validation Scores:", scores_logistic)
print("Random Forest Cross-Validation Scores:", scores_rf)
print("SVM Cross-Validation Scores:", scores_svm)