from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the breast cancer Wisconsin dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Instantiate the PCA model
pca = PCA()

# Fit the model to the data
pca.fit(X)

# Transform the data to the principal components
X_pca = pca.transform(X_scaled)

# Create a KMeans model with 3 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(X_pca)

# Predict the cluster labels for each data point
labels = kmeans.predict(X_pca)

# Plot the results
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
