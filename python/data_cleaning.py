import pandas as pd
import os

raw_path = "data/raw/online_retail.csv"
processed_path = "data/processed/cleaned_retail_data.csv"

df = pd.read_csv(raw_path, encoding="ISO-8859-1")

df.columns = df.columns.str.strip()

df = df.dropna(subset=["Customer ID"])

df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Customer ID"] = df["Customer ID"].astype(int)

df["TotalAmount"] = df["Quantity"] * df["Price"]

df = df.drop_duplicates()

os.makedirs("data/processed", exist_ok=True)

df.to_csv(processed_path, index=False)

print("Data cleaning completed")
print("Rows after cleaning:", len(df))
print("Saved file:", processed_path)