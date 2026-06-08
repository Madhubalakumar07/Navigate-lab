import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"D:\Navigate lab\Datasets\Mall_Customers.csv")
print(data.head())
data.drop(['CustomerID', 'Gender', 'Age'], axis='columns', inplace=True)

# Prepare data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Train DBSCAN model
dbscan = DBSCAN(eps=0.5, min_samples=15)
data['Cluster'] = dbscan.fit_predict(data_scaled)
print(data.head())

# Visualize clusters
plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'], c=data['Cluster'])
plt.title('DBSCAN Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()