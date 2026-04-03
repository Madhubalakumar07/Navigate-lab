import joblib
# Load the model from the file
model = joblib.load('diamond_price_model.pkl')
# Make a prediction using the loaded model
res = model.predict([[1.7, 3, 2, 7]])
print(res)