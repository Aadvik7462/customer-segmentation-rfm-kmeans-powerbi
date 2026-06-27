USE CustomerSegmentationDB;
GO

CREATE VIEW vw_customer_segments AS
SELECT
    CustomerID,
    Recency,
    Frequency,
    Monetary,
    Cluster,
    Segment
FROM customer_segments;
GO