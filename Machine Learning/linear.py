import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_excel("D:\\Navigate lab\\Datasets\\sample.xlsx")
print(data.head())
lr = LinearRegression()
x = data[['price']]
y = data['weight']
lr.fit(x, y)
print(lr.predict(pd.DataFrame({'price':[25000]})))
plt.scatter(x, y)
plt.plot(x, lr.predict(x))
plt.xlabel("Weight")
plt.ylabel("Price")
plt.show()