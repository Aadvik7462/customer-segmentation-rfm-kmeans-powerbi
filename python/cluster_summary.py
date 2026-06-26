import pandas as pd

df = pd.read_csv("data/processed/customer_segments.csv")

summary = (
    df.groupby("Cluster")[["Recency", "Frequency", "Monetary"]]
      .mean()
      .round(2)
)

print("\nCluster Summary\n")
print(summary)

summary.to_csv(
    "data/processed/cluster_summary.csv"
)

print("\nCluster summary saved successfully.")