import pandas as pd

# Load clustered data
df = pd.read_csv("data/processed/customer_segments.csv")

# Assign business names
segment_names = {
    0: "Loyal Customers",
    1: "Lost Customers",
    2: "Champions",
    3: "High Value Customers"
}

df["Segment"] = df["Cluster"].map(segment_names)

# Save updated file
df.to_csv(
    "data/processed/customer_segments_final.csv",
    index=False
)

print("\nCustomer Segments Assigned Successfully!\n")

print(df[["Customer ID", "Cluster", "Segment"]].head())

print("\nSegment Distribution:\n")
print(df["Segment"].value_counts())