--1
select SalesOrderID, ShipDate 
from Sales.SalesOrderHeader
where ShipDate between '7/28/2002' and '7/29/2014';

--2
select ProductID, Name
from Production.Product
where StandardCost < 110;

--3
select ProductID , name
from Production.Product
where Weight is null;


--4
select ProductID , name
from Production.Product
where color in ('silver', 'black', 'red');

--5
select name
from Production.Product
where name like 'b%';

--6
UPDATE Production.ProductDescription 
SET Description = 'Chromoly steel_High of defects' 
WHERE ProductDescriptionID = 3

select description
from Production.ProductDescription
where Description like '%[_]%';

--7
select sum(totalDue) as [sum of TotalDue] , orderDate
from Sales.SalesOrderHeader 
where OrderDate between '7/01/2001' and '7/31/2014'
group by OrderDate;

--8
select distinct HireDate
from HumanResources.Employee;

--9
select avg(distinct listPrice)
from Production.Product;

--10
select concat('The ', name, ' is only! ', listPrice)
from Production.Product
where listPrice between 100 and 120
order by ListPrice;


---------------------------------------

--part 2
--11
--12
--DONEEEE


