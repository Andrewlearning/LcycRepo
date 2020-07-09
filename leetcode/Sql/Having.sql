--O_Id	OrderDate	OrderPrice	Customer
--1	2008/12/29	    1000	       Bush
--2	2008/11/23	    1600	     Carter
--3	2008/10/05	    700	           Bush
--4	2008/09/28	    300	           Bush
--5	2008/08/06	    2000	      Adams
--6	2008/07/21	    100	         Carter

--现在，我们希望查找订单总金额少于 2000 的客户。
SELECT
    customer,sum(OrderPrice)
FROM
    Orders
GROUP BY
    customer
HAVING
    SUM(OrderPrice)<2000

--Customer	SUM(OrderPrice)
--Carter	    1700




--现在我们希望查找客户 "Bush" 或 "Adams" 拥有超过 1500 的订单总金额。
--我们在 SQL 语句中增加了一个普通的 WHERE 子句：

SELECT
    Customer,SUM(OrderPrice)
FROM
    Orders
WHERE
    Customer='Bush' or Customer='Adams'
GROUP BY
    Customer
HAVING
    SUM(OrderPrice)>1500

--Customer	SUM(OrderPrice)
--Bush	    2000
--Adams	    2000