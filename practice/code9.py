import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
horsepower = np.round(np.random.uniform(20, 70, 100), 2)
weight = np.round(np.random.uniform(100, 200, 100), 2)
mpg = 15 + 50 * (horsepower ** -0.5) * (weight ** -0.3) + np.random.normal(0, 1, 100)
bikes = pd.DataFrame({'horsepower': horsepower, 'weight': weight, 'mpg': mpg})
print(bikes["mpg"].mean())
plt.scatter(bikes['horsepower'], bikes['mpg'])
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.title('MPG vs Horsepower')
plt.show()