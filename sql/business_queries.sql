SELECT
    Segment,
    COUNT(*) AS TotalCustomers
FROM customer_segments
GROUP BY Segment
ORDER BY TotalCustomers DESC;


SELECT
    Segment,
    SUM(Monetary) AS TotalRevenue
FROM customer_segments
GROUP BY Segment
ORDER BY TotalRevenue DESC;

SELECT
    Segment,
    AVG(Recency) AS AverageRecency
FROM customer_segments
GROUP BY Segment;

SELECT
    Segment,
    AVG(Frequency) AS AverageFrequency
FROM customer_segments
GROUP BY Segment;

SELECT TOP 10
    CustomerID,
    Segment,
    Monetary
FROM customer_segments
ORDER BY Monetary DESC;