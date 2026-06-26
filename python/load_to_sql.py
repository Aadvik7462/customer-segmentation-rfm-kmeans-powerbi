import pandas as pd
from sqlalchemy import create_engine

server = "localhost"
database = "CustomerSegmentationDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
)

engine = create_engine(connection_string)

df = pd.read_csv("data/processed/customer_segments_final.csv")

df = df.rename(columns={
    "Customer ID": "CustomerID"
})

df.to_sql(
    name="customer_segments",
    con=engine,
    if_exists="append",
    index=False
)

print("Customer segments loaded successfully!")
print("Rows loaded:", len(df))