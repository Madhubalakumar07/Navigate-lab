import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

# Load dataset

iris = load_iris()
data = iris.data
data_df = pd.DataFrame(data, columns=iris.feature_names)
data_df = data_df.drop(columns=['sepal length (cm)', 'sepal width (cm)'])
print(data_df.head())

# Initialize KMeans

km = KMeans(n_clusters=3)

# Fit the model

km.fit(data_df)
y_km = km.predict(data_df)
print(y_km)
data_df['cluster'] = y_km
df1 = data_df[data_df['cluster'] == 0]
df2 = data_df[data_df['cluster'] == 1]
df3 = data_df[data_df['cluster'] == 2]
centroids = km.cluster_centers_
print(centroids)

# Plotting

plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color='red', label='Cluster 1')
plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], color='blue', label='Cluster 2')
plt.scatter(df3['petal length (cm)'], df3['petal width (cm)'], color='green', label='Cluster 3')
plt.scatter(centroids[:, 0], centroids[:, 1], color='yellow', marker='X', s=200, label='Centroids')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('K-Means Clustering of Iris Dataset')
plt.legend()
plt.show()

# Elbow method to find optimal number of clusters

sse = []
for i in range(1,10):
    km = KMeans(n_clusters=i)
    km.fit(data_df.drop(columns=['cluster']))
    sse.append(km.inertia_)
plt.plot(range(1,10), sse, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
plt.title('Elbow Method for Optimal Clusters')
plt.show()