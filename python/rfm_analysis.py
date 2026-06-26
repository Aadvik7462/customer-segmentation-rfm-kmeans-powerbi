import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_retail_data.csv")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Latest date in dataset
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Create RFM Table
rfm = df.groupby("Customer ID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "Invoice": "nunique",
    "TotalAmount": "sum"
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

# Save output
os.makedirs("data/processed", exist_ok=True)
rfm.to_csv("data/processed/rfm_table.csv")

print("\nRFM Table Created Successfully!\n")
print(rfm.head())

print("\nTotal Customers:", len(rfm))