-- ============================================
-- CHINOOK DATABASE - SQL PRACTICE WORKBOOK
-- Topics: Joins, Aggregations, Filtering
-- ============================================

-- Level 1 – Basic Joins
-- List of clients and the country where they live
SELECT FirstName, LastName, Country
FROM Customer
LIMIT 10;

-- Name of each album and the artist who recorded it
SELECT al.AlbumId, al.Title AS AlbumTitle, ar.Name AS ArtistName
FROM Album AS al
JOIN Artist AS ar 
    ON al.ArtistId = ar.ArtistId;

-- Level 2 – Joins + Filters
-- List of songs by a specific artist
SELECT t.TrackId, t.Name AS TrackName, al.Title AS AlbumTitle, ar.Name AS ArtistName
FROM Track AS t
JOIN Album AS al ON t.AlbumId = al.AlbumId
JOIN Artist AS ar ON al.ArtistId = ar.ArtistId
WHERE ar.Name = 'AC/DC';

-- Customers from Brazil and their invoices
SELECT c.CustomerId, c.FirstName, c.LastName, 
    i.InvoiceId, i.InvoiceDate, i.Total
FROM Customer as c 
JOIN Invoice as i 
ON c.CustomerId = i.CustomerId
WHERE Country = 'Brazil';

-- Level 3 – Aggregations
-- Number of songs per genre
SELECT g.Name AS GenreName,
    COUNT(t.TrackId) AS TrackCount
FROM Track AS t
JOIN Genre AS g 
    ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY g.Name ASC;

-- Total sales by country
SELECT c.Country,
    SUM(i.Total) AS TotalSales
FROM Customer AS c
JOIN Invoice AS i 
    ON c.CustomerId = i.CustomerId
GROUP BY c.Country
ORDER BY TotalSales DESC;


-- Level 4 – Joins + Advanced Aggregations
-- Artist with the most songs in the database
SELECT ar.Name AS ArtistName,
    COUNT(t.TrackId) AS TrackCount
FROM Artist AS ar
JOIN Album AS al 
    ON ar.ArtistId = al.ArtistId
JOIN Track AS t 
    ON al.AlbumId = t.AlbumId
GROUP BY ar.ArtistId
ORDER BY TrackCount DESC;
-- LIMIT 1;


-- Top 5 customers who have spent the most
SELECT c.CustomerId,
    c.FirstName || ' ' || c.LastName AS FullName,
    SUM(i.Total) AS TotalSpent
FROM Customer AS c
JOIN Invoice AS i 
    ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 5;


-- Average length (in seconds) of songs by artist
SELECT ar.Name AS ArtistName,
    ROUND(AVG(t.Milliseconds) / 1000, 2) AS AvgDurationSeconds
FROM Artist AS ar
JOIN Album AS al 
    ON ar.ArtistId = al.ArtistId
JOIN Track AS t 
    ON al.AlbumId = t.AlbumId
GROUP BY ar.ArtistId
ORDER BY AvgDurationSeconds DESC;