--task1--
create database TechShop;
use TechShop;

create table customers (
    customerid int primary key,
    firstname varchar(50),
    lastname varchar(50),
    email varchar(50),
    phone varchar(20),
    address varchar(150));

create table products (
    productid int primary key,
    productname varchar(100),
    description text,
    price decimal(10,2));

create table orders (
    orderid int primary key,
    customerid int,
    orderdate date,
    totalamount decimal(10,2),
    foreign key (customerid) references customers(customerid));

create table orderdetails (
    orderdetailid int primary key,
    orderid int,
    productid int,
    quantity int,
    foreign key (orderid) references orders(orderid),
    foreign key (productid) references products(productid));

create table inventory (
    inventoryid int primary key,
    productid int,
    quantityinstock int,
    laststockupdate date,
    foreign key (productid) references products(productid));

insert into customers values
(1, 'Nithya', 'Sree', 'nithya@gmail.com', '1234567890', 'chennai'),
(2, 'Benita', 'sherina', 'benny@gmail.com', '2345678981', 'california'),
(3, 'charu', 'latha', 'charu@gmail.com', '5456789012', 'agra'),
(4, 'diana', 'prince', 'diana@gmail.com', '4568890123', 'new york'),
(5, 'Pavithra', 'devi', 'pavi@gmail.com', '3458901234', 'german'),
(6, 'kavya', 'shree', 'kavya@gmail.com', '6789012345', 'chicago'),
(7, 'jobitha', 'lakshmi', 'jobitha1@gmail.com', '7890123456', 'maharasthra'),
(8, 'hema', 'varshini', 'hema@gmail.com', '8901234567', 'france'),
(9, 'jaya', 'shree', 'jaya@gmail.com', '9012345678', 'chennai'),
(10, 'jerlin', 'priyadharshini', 'jerlin@gmail.com', '9123456789', 'delhi');

insert into products values
(1, 'laptop', '12 inch business laptop', 65000.00),
(2, 'mouse', 'wireless optical mouse', 1200.00),
(3, 'keyboard', 'advanced  keyboard', 2500.00),
(4, 'monitor', '24 inch full hd', 10000.00),
(5, 'printer', 'all-in-one printer', 8000.00),
(6, 'router', ' wifi router', 3000.00),
(7, 'webcam', '1080p hd webcam', 3500.00),
(8, 'speaker', 'bluetooth portable speaker', 3500.00),
(9, 'headphones', 'advanced headphones with good audio support', 5000.00),
(10, 'hard disk', 'external hard disk', 4500.00);

insert into orders values
(1, 1, '2024-05-01', 60000),
(2, 2, '2024-05-02', 3700),
(3, 3, '2024-05-03', 15000),
(4, 4, '2024-05-04', 8500),
(5, 5, '2024-05-05', 3500),
(6, 6, '2024-05-06', 14500),
(7, 7, '2024-05-07', 1200),
(8, 8, '2024-05-08', 10000),
(9, 9, '2024-05-09', 3000),
(10, 10, '2024-05-10', 9500);

insert into orderdetails values
(1, 1, 1, 1),
(2, 2, 2, 1),
(3, 3, 4, 1),
(4, 4, 5, 1),
(5, 5, 8, 1),
(6, 6, 10, 2),
(7, 7, 3, 1),
(8, 8, 4, 1),
(9, 9, 6, 3),
(10, 10, 9, 2);

insert into inventory values
(1, 1, 20, '2024-03-25'),
(2, 2, 50, '2024-03-26'),
(3, 3, 30, '2024-03-27'),
(4, 4, 25, '2024-03-28'),
(5, 5, 15, '2024-03-29'),
(6, 6, 40, '2024-03-30'),
(7, 7, 22, '2024-03-31'),
(8, 8, 18, '2024-05-01'),
(9, 9, 35, '2024-05-02'),
(10, 10, 28, '2024-05-03');

--task 2--
--1- to retrive names and email from customer
select firstname,lastname ,email from customers;

--2-- list all order with date and cus name
select o.orderid,o.orderdate,c.firstname,c.lastname from orders o
join customers c on c.customerid = o.customerid;

--3--insert a new query in customer
insert into customers values (11, 'saratha', 'priya', 'sara@example.com', '9888887776', '45, park avenue');

--4--update price by +10% in product 
update products set price = price * 1.10;

--5--delete order and orderdetail from o and od 
delete from orderdetails where orderid = 1;
delete from orders where orderid = 1;

--6-- insert into orders
insert into orders values(11,11,'2024-05-25',7000);

--7--update contact info in customer 
update customers
set email = 'nithya3@gmail.com',
    address = 'abccc',
    phone = '9876543456'
where customerid = 1;

--8-- recalculate and update tot in orders 
update orders
set totalamount = (
    select sum(od.quantity * p.price)
    from orderdetails od
    join products p on od.productid = p.productid
    where od.orderid = orders.orderid);

--9-- delete all orders and od
delete from orderdetails
where orderid in (select orderid from orders where customerid = 4);
delete from orders
where customerid = 4;

--10--insert into product
insert into products values(11,'xyz','aaaabbbbccc',4000);

--11--update status
alter table orders add status varchar(50);
update orders
set status = 'delivered' where orderid =2;

--12--cal and up no of orders by cus in order tab
alter table customers Add number_of_orders int;
update customers
set number_of_orders = (select count(*) from orders 
where orders.customerid = customers.customerid);

---task 3--
--1-- all order with cus info 
select o.orderid,c.customerid,c.firstname,c.lastname,o.orderdate,o.totalamount 
from orders o
join customers c on o.customerid = c.customerid;

--2--total revenue for gadget 
select p.productname,sum(od.quantity*p.price) as Total_Revenue 
from orderdetails od
join products p on od.productid = p.productid
group by p.productname;

--3--list all customer with 1 purchase
select distinct c.customerid,c.firstname,c.lastname,c.email,c.phone
from customers c
join orders o  on c.customerid = o.customerid;

--4-- popular e-gad 
select top 1 
    p.productname,
    sum(od.quantity) as total_quantity
from orderdetails od
join products p on od.productid = p.productid
group by p.productname
order by total_quantity desc;

--5--e-gad
select p.productid,p.productname,p.description,p.price 
from products p

--6-- avg ord val from cus
select c.customerid,c.firstname ,c.lastname ,
avg(o.totalamount) as Total_value
from customers c
join orders o on c.customerid = o.customerid
group by c.customerid,c.firstname ,c.lastname;

--7-- hig total revenue
select top 1 
	o.orderid,o.orderdate,o.totalamount,c.customerid,c.firstname,c.lastname 
from orders o
join customers c  on o.customerid= c.customerid
order by o.totalamount desc;

--8--list number and electronic gadgedt
select p.productname,count(od.orderdetailid) as total_orders
from products p
join orderdetails od on p.productid = od.productid
group by p.productname
order by p.productname;

--9.--specif product by customer
select distinct c.firstname,c.lastname,c.email
from customers c
join orders o on c.customerid = o.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where p.productname = 'mouse';

--10--total revenue 
select sum(totalamount) as total_revenue
from orders
where orderdate between '2024-03-01' and '2024-12-31';

---task 4--
--1--customers with no order
select c.customerid,c.firstname,c.lastname 
from customers c
where customerid not in (select customerid from orders);

--2--total products for sale
select count(*) as Total_products 
from products;

--3--total revenue by techshop
select sum(totalamount) as TotalRevenue 
from orders;

--4--avg quantity 
select avg(od.quantity) as AvgQuantity
from orderdetails od
join products p on od.productid=p.productid
where p.productname ='mouse';

--5--total revenue for specific customer
select sum(totalamount) as customer_revenue
from orders
where customerid = 3;

--6--customers with more order
select c.firstname,c.lastname,count(o.orderid) as total_count 
	from customers c
	join orders o on c.customerid =o.customerid 
	group by c.customerid,c.firstname,c.lastname;

--7--pop category

select top 1
	p.productname,count(od.quantity) as Totalquantity 
	from orderdetails od
	join products p on od.productid =p.productid
	group by p.productname
	order by Totalquantity desc;

--8--high revenue
select top 1
c.customerid,c.firstname,c.lastname,sum(o.totalamount)as Highamount
from customers c
join orders o on c.customerid = o.customerid
group by c.customerid,c.firstname,c.lastname
order by Highamount desc;

--9--avg ord val
select sum(totalamount) * 1.0 / count(*) as average_order_value
from orders;

--10--order with c name
select c.firstname,c.lastname ,count(o.orderid)as Ordervalue 
from customers c
join orders o on c.customerid = o.customerid
group by c.customerid,c.firstname,c.lastname;




