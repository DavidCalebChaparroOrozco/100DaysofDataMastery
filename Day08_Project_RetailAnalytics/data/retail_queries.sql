-- Basic Business Metrics

-- Total Revenue with formatted output
SELECT 
    SUM(TotalAmount) AS TotalRevenue,
    COUNT(DISTINCT CustomerID) AS UniqueCustomers,
    COUNT(TransactionID) AS TotalTransactions
FROM retail_sales

-- Monthly Sales Performance with growth calculation
WITH monthly_data AS (
    SELECT 
        strftime('%Y-%m', Date) AS Month,
        SUM(TotalAmount) AS MonthlySales,
        LAG(SUM(TotalAmount)) OVER (ORDER BY strftime('%Y-%m', Date)) AS PrevMonthSales
    FROM retail_sales
    GROUP BY Month
)
SELECT
    Month,
    MonthlySales,
    PrevMonthSales,
    ROUND((MonthlySales*1.0 - PrevMonthSales) / PrevMonthSales * 100, 2) AS GrowthRate
FROM monthly_data
ORDER BY Month

-- Create a customer summary table in the database
CREATE TABLE IF NOT EXISTS customer_summary AS
SELECT
    CustomerID,
    Gender,
    Age,
    COUNT(TransactionID) AS TransactionCount,
    SUM(TotalAmount) AS TotalSpent,
    MIN(Date) AS FirstPurchaseDate,
    MAX(Date) AS LastPurchaseDate,
    JULIANDAY(MAX(Date)) - JULIANDAY(MIN(Date)) AS CustomerTenureDays
FROM retail_sales
GROUP BY CustomerID, Gender, Age

-- Verify the table was created
SELECT *
FROM customer_summary
LIMIT 5;

-- Customer summary table schema:
PRAGMA table_info(customer_summary);

-- First 5 records
SELECT * FROM customer_summary LIMIT 5;

-- Customer segmentation analysis
SELECT
    CASE
        WHEN TotalSpent > 2000 THEN 'VIP'
        WHEN TotalSpent > 1000 THEN 'Premium'
        WHEN TotalSpent > 500 THEN 'Standard'
        ELSE 'Basic'
    END AS CustomerTier,
    COUNT(*) AS CustomerCount,
    SUM(TotalSpent) AS TotalRevenue,
    AVG(TotalSpent) AS AvgSpend,
    AVG(TransactionCount) AS AvgTransactions
FROM customer_summary
GROUP BY CustomerTier
ORDER BY TotalRevenue DESC

-- Create product_performance table
CREATE TABLE IF NOT EXISTS product_performance AS
    SELECT
        ProductCategory,
        COUNT(TransactionID) AS TransactionCount,
        SUM(Quantity) AS TotalUnitsSold,
        SUM(TotalAmount) AS TotalRevenue,
        AVG(PricexUnit) AS AvgPrice,
        SUM(TotalAmount) / SUM(Quantity) AS RevenuePerUnit
    FROM retail_sales
    GROUP BY ProductCategory

-- Verify table creation
SELECT name FROM sqlite_master WHERE type='table' AND name='product_performance'

-- Create index
CREATE INDEX IF NOT EXISTS idx_product_category ON product_performance(ProductCategory)

-- Verify index creation
SELECT * FROM sqlite_master WHERE type = 'index' AND tbl_name = 'product_performance';

-- Product perfomance table created
SELECT *
FROM product_performance;