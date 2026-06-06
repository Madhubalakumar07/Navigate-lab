import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import LabelEncoder
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"D:\Navigate lab\Datasets\Mall_Customers.csv")
print(data.head())
data.drop(['CustomerID'], axis='columns', inplace=True)

# Prepare data
le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])

# Find optimal number of clusters using dendrogram
linked = linkage(data, method='ward')
dendrogram(linked)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distances')
plt.show()

# Train Agglomerative Clustering model
hc = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')
data['Cluster'] = hc.fit_predict(data)
print(data.head())