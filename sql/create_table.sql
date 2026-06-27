USE CustomerSegmentationDB;
GO

CREATE TABLE customer_segments
(
    CustomerID INT PRIMARY KEY,
    Recency INT,
    Frequency INT,
    Monetary DECIMAL(12,2),
    Cluster INT,
    Segment VARCHAR(50)
);
GO