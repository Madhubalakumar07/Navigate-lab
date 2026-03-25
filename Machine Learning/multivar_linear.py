import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_excel("D:\\Navigate lab\\Datasets\\sample.xlsx")
print(data.head())
lr = LinearRegression()
x = data[['Carat', 'Cut_Score', 'Color_Score', 'Clarity_Score']]
y = data['Price_USD']
lr.fit(x, y)
print(lr.coef_)
print(lr.intercept_)
res = lr.predict(pd.DataFrame([[1.7, 4, 4, 7]]))
print(res)
plt.scatter(data['Carat'], data['Price_USD'], color='blue')
plt.scatter(data['Cut_Score'], data['Price_USD'], color='red')  
plt.scatter(data['Color_Score'], data['Price_USD'], color='green')  
plt.scatter(data['Clarity_Score'], data['Price_USD'], color='orange')
plt.xlabel('Features')
plt.ylabel('Price (USD)')
plt.title('Multivariate Linear Regression')
plt.legend(['Carat', 'Cut_Score', 'Color_Score', 'Clarity_Score'])
plt.show()