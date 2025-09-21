SELECT 
    h.OrderDate,
    h.SalesOrderID,
    d.LineTotal AS TotalDue,
    sp.Name AS Region,
    p.Name AS Product
FROM 
    Sales.SalesOrderDetail d
INNER JOIN 
    Sales.SalesOrderHeader h ON d.SalesOrderID = h.SalesOrderID
INNER JOIN 
    Person.Address a ON h.ShipToAddressID = a.AddressID
INNER JOIN 
    Person.StateProvince sp ON a.StateProvinceID = sp.StateProvinceID
INNER JOIN 
    Production.Product p ON d.ProductID = p.ProductID;