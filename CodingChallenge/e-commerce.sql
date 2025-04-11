create database ec;
use ec;

create table customers (
    customer_id int primary key,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100),
    address varchar(255));

create table products (
    product_id int primary key,
    name varchar(100),
    description varchar(255),
    price decimal(10,2),
    stock_quantity int);

create table cart (
    cart_id int primary key,
    customer_id int,
    product_id int,
    quantity int,
    foreign key (customer_id) references customers(customer_id),
    foreign key (product_id) references products(product_id));

create table orders (
    order_id int primary key,
    customer_id int,
    order_date date,
    total_amount decimal(10,2),
    foreign key (customer_id) references customers(customer_id));

create table order_items (
    order_item_id int primary key,
    order_id int,
    product_id int,
    quantity int,
    item_amount decimal(10,2),
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id));

insert into customers values
(1, 'John', 'Doe', 'johndoe@example.com', '123 Main St, City'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '456 Elm St, Town'),
(3, 'Robert', 'Johnson', 'robert@example.com', '789 Oak St, Village'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '101 Pine St, Suburb'),
(5, 'David', 'Lee', 'david@example.com', '234 Cedar St, District'),
(6, 'Laura', 'Hall', 'laura@example.com', '567 Birch St, County'),
(7, 'Michael', 'Davis', 'michael@example.com', '890 Maple St, State'),
(8, 'Emma', 'Wilson', 'emma@example.com', '321 Redwood St, Country'),
(9, 'William', 'Taylor', 'william@example.com', '432 Spruce St, Province'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '765 Fir St, Territory');

insert into products values
(1, 'Laptop', 'High-performance laptop', 1600.00, 10),
(2, 'Smartphone', 'Latest smartphone', 800.00, 10),
(3, 'Tablet', 'Portable tablet', 600.00, 15),
(4, 'Headphones', 'Noise-canceling', 300.00, 20),
(5, 'TV', '4K Smart TV', 150.00, 30),
(6, 'Coffee Maker', 'Automatic coffee maker', 50.00, 25),
(7, 'Refrigerator', 'Energy-efficient', 700.00, 10),
(8, 'Microwave Oven', 'Countertop microwave', 80.00, 15),
(9, 'Blender', 'High-speed blender', 70.00, 20),
(10, 'Vacuum Cleaner', 'Bagless vacuum cleaner', 120.00, 10);

insert into orders values
(1, 1, '2023-01-05', 1200.00),
(2, 2, '2023-02-10', 900.00),
(3, 3, '2023-03-15', 300.00),
(4, 4, '2023-04-20', 150.00),
(5, 5, '2023-05-25', 1800.00),
(6, 6, '2023-06-30', 400.00),
(7, 7, '2023-07-05', 700.00),
(8, 8, '2023-08-10', 160.00),
(9, 9, '2023-09-15', 140.00),
(10, 10, '2023-10-20', 1400.00);

insert into order_items values
(1, 1, 1, 2, 1600.00),
(2, 1, 3, 1, 300.00),
(3, 2, 2, 3, 1800.00),
(4, 3, 5, 2, 1800.00),
(5, 4, 4, 4, 600.00),
(6, 4, 6, 1, 50.00),
(7, 5, 1, 1, 800.00),
(8, 5, 2, 2, 1200.00),
(9, 6, 10, 2, 240.00),
(10, 6, 9, 3, 210.00);

insert into cart values
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 3),
(4, 3, 4, 4),
(5, 3, 5, 2),
(6, 4, 6, 1),
(7, 5, 1, 1),
(8, 6, 10, 2),
(9, 6, 9, 3),
(10, 7, 7, 2);

---Queries---
--1. Update refrigerator product price to 800. 
update products
set price = 800.00
where name='Refrigerator';

--2. Remove all cart items for a specific customer. 
delete from cart
where customer_id =3;

--3. Retrieve Products Priced Below $100. 
select *from products
where price < 100;

--4. Find Products with Stock Quantity Greater Than 5. 
select*from products
where stock_quantity > 5;

--5. Retrieve Orders with Total Amount Between $500 and $1000. 
select *from orders
where total_amount between 500 and 1000;

--6. Find Products which name end with letter ‘r’.
select *from products
where name like '%r';

--7. Retrieve Cart Items for Customer 5. 
select *from cart
where customer_id =5;

--8. Find Customers Who Placed Orders in 2023. 
select distinct c.customer_id,c.first_name,c.last_name,c.email
from customers c
join orders o on c.customer_id= o.customer_id
where year(o.order_date) = 2023;

--9. Determine the Minimum Stock Quantity for Each Product Category
select top 1 
name, stock_quantity
from products
order by stock_quantity asc;

--10. Calculate the Total Amount Spent by Each Customer. 
select c.customer_id,c.first_name,c.last_name,sum(o.total_amount) as Total_Amount
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.first_name, c.last_name;

--11. Find the Average Order Amount for Each Customer. 
select c.customer_id,c.first_name,c.last_name,avg(o.total_amount)as Avg_Amount
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.first_name, c.last_name;

--12. Count the Number of Orders Placed by Each Customer. 
select c.customer_id, c.first_name, c.last_name, count(o.order_id) as Num_Orders
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.first_name, c.last_name;

--13. Find the Maximum Order Amount for Each Customer. 
select c.customer_id, c.first_name, c.last_name, max(o.total_amount) as Max_Order_Amount
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.first_name, c.last_name;

--14. Get Customers Who Placed Orders Totaling Over $1000.
select c.customer_id, c.first_name, c.last_name, sum(o.total_amount) as Total_Amount
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.first_name, c.last_name
having sum(o.total_amount) > 1000;

--15. Subquery to Find Products Not in the Cart. 
select name, product_id
from products
where product_id not in (
    select product_id from cart);

--16. Subquery to Find Customers Who Haven't Placed Orders. 
select customer_id,first_name,last_name,email
from customers
where customer_id not in (
    select customer_id from orders);

--17. Subquery to Calculate the Percentage of Total Revenue for a Product. 
select p.product_id,name,
cast(sum(item_amount) * 100.0 / 
(select sum(item_amount) from order_items)as decimal(10, 2))as Revenue_percent
from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_id, name; 

--or--

select p.product_id, p.name, 
 sum(oi.item_amount) * 100.0 / (select sum(item_amount) from order_items)as revenue_percentage
from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_id, p.name;

--18. Subquery to Find Products with Low Stock.
select product_id,name,stock_quantity
from products
where stock_quantity < (
    select avg(stock_quantity) from products);

--19. Subquery to Find Customers Who Placed High-Value Orders.
select customer_id, first_name, last_name, email
from customers
where customer_id in (
    select top 3 customer_id
    from orders
    order by total_amount desc);


















