SELECT COUNT(*) FROM superstore;

SELECT SUM(Sales) FROM superstore;

SELECT SUM(Profit) FROM superstore;

SELECT Category, SUM(Sales)
FROM superstore
GROUP BY Category;

SELECT Region, SUM(Sales)
FROM superstore
GROUP BY Region;

SELECT Product_Name, SUM(Sales)
FROM superstore
GROUP BY Product_Name
ORDER BY SUM(Sales) DESC
LIMIT 5;