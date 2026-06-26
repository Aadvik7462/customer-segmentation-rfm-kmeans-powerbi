import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load RFM table
rfm = pd.read_csv("data/processed/rfm_table.csv")

# Preserve Customer ID
customer_ids = rfm["Customer ID"]

# Features for clustering
X = rfm[["Recency", "Frequency", "Monetary"]]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train K-Means
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(X_scaled)

# Save clustered data
os.makedirs("data/processed", exist_ok=True)

rfm.to_csv(
    "data/processed/customer_segments.csv",
    index=False
)

print("\nCustomer Segmentation Completed!\n")

print(rfm.head())

print("\nCluster Distribution:\n")
print(rfm["Cluster"].value_counts().sort_index())