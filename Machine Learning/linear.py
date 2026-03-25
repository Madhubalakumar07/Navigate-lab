import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_excel("D:\\Navigate lab\\Datasets\\sample.xlsx")
print(data.head())
lr = LinearRegression()
x = data[['Price_USD']]
y = data['Carat']
lr.fit(x, y)
print(lr.predict(pd.DataFrame({'Price_USD':[25000]})))
plt.scatter(x, y)
plt.plot(x, lr.predict(x))
plt.xlabel("Price (USD)")
plt.ylabel("Carat")
plt.show()