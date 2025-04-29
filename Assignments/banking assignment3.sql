create database hmbank;
use hmbank;


create table customers (
    customer_id int primary key identity(1,1),
    first_name varchar(50),
    last_name varchar(50),
    dob date,
    email varchar(100),
    phone_number varchar(15),
    address varchar(255));
SELECT * FROM Customers;
SELECT * FROM Customers WHERE first_name = 'Nithya';


create table accounts (
    account_id int primary key identity(1001,1),
    customer_id int,
    account_type varchar(20),
    balance decimal(12,2),
    foreign key (customer_id) references customers(customer_id));

create table transactions (
    transaction_id int primary key identity(1,1),
    account_id int,
    transaction_type varchar(20),
    amount decimal(12,2),
    transaction_date datetime default getdate(),
    foreign key (account_id) references accounts(account_id));

--task 2
insert into customers (first_name, last_name, dob, email, phone_number, address)
values
('john', 'doe', '1980-01-15', 'john.doe@example.com', '9876543210', 'new york'),
('jane', 'smith', '1990-03-22', 'jane.smith@example.com', '9123456789', 'los angeles'),
('alice', 'brown', '1975-06-10', 'alice.brown@example.com', '9988776655', 'chicago'),
('bob', 'johnson', '1985-12-05', 'bob.johnson@example.com', '9988123456', 'houston'),
('tom', 'harris', '1992-04-30', 'tom.harris@example.com', '8877665544', 'phoenix'),
('emily', 'davis', '1998-11-12', 'emily.davis@example.com', '9988441122', 'san francisco'),
('chris', 'lee', '1982-08-19', 'chris.lee@example.com', '9988112233', 'seattle'),
('sophia', 'wilson', '1995-01-23', 'sophia.wilson@example.com', '9784561230', 'austin'),
('david', 'clark', '1988-09-14', 'david.clark@example.com', '9123459876', 'denver'),
('olivia', 'martin', '1979-07-29', 'olivia.martin@example.com', '9112345678', 'boston');

insert into accounts (customer_id, account_type, balance)
values
(1, 'savings', 1500.00),
(2, 'current', 2500.00),
(3, 'savings', 500.00),
(4, 'current', 1200.00),
(5, 'savings', 1000.00),
(6, 'zero_balance', 0.00),
(7, 'savings', 3500.00),
(8, 'current', 4000.00),
(9, 'savings', 750.00),
(10, 'savings', 1800.00);

insert into transactions (account_id, transaction_type, amount)
values
(1001, 'deposit', 500.00),
(1002, 'withdrawal', 300.00),
(1003, 'deposit', 100.00),
(1004, 'deposit', 200.00),
(1005, 'withdrawal', 100.00),
(1006, 'deposit', 0.00),
(1007, 'deposit', 1000.00),
(1008, 'withdrawal', 500.00),
(1009, 'deposit', 300.00),
(1010, 'withdrawal', 100.00);

-- 1. retrieve the name, account type, and email of all customers
select concat(first_name, ' ', last_name) as full_name, account_type, email
from customers
join accounts on customers.customer_id = accounts.customer_id;

-- 2. list all transactions corresponding to each customer
select t.transaction_id, c.first_name, c.last_name, a.account_type, t.transaction_type, t.amount, t.transaction_date
from transactions t
join accounts a on t.account_id = a.account_id
join customers c on a.customer_id = c.customer_id;

-- 3. increase the balance of a specific account by a certain amount
update accounts
set balance = balance + 500
where account_id = 1001;

-- 4. combine first and last names of customers as a full name
select concat(first_name, ' ', last_name) as full_name
from customers;

-- 5. remove accounts with a balance of zero where the account type is savings
delete from accounts
where balance = 0 and account_type = 'savings';

-- 6. find customers living in a specific city (e.g., new york)
select * from customers
where address like '%new york%';

-- 7. get the account balance for a specific account
select balance from accounts
where account_id = 1001;

-- 8. list all current accounts with a balance greater than $1,000
select * from accounts
where account_type = 'current' and balance > 1000;

-- 9. retrieve all transactions for a specific account
select * from transactions
where account_id = 1001;

-- 10. calculate the interest accrued on savings accounts based on a given interest rate (4.5%)
select account_id, balance, balance * 0.045 as interest
from accounts
where account_type = 'savings';

-- 11. identify accounts where the balance is less than a specified overdraft limit
select * from accounts
where balance < 500;

-- 12. find customers not living in a specific city (e.g., boston)
select * from customers
where address not like '%boston%';

--task 3
-- 1. find the average account balance for all customers
select avg(balance) as average_balance
from accounts;

-- 2. retrieve the top 10 highest account balances
select top 10 *
from accounts
order by balance desc;

-- 3. calculate total deposits for all customers on a specific date (example: '2025-04-01')
select sum(amount) as total_deposits
from transactions
where transaction_type = 'deposit'
and cast(transaction_date as date) = '2025-04-01';

-- 4. find the oldest and newest customers
select * from customers
order by dob asc; 

select * from customers
order by dob desc; 

-- 5. retrieve transaction details along with the account type
select t.*, a.account_type
from transactions t
join accounts a on t.account_id = a.account_id;

-- 6. get a list of customers along with their account details
select c.*, a.account_id, a.account_type, a.balance
from customers c
join accounts a on c.customer_id = a.customer_id;

-- 7. retrieve transaction details along with customer information for a specific account (e.g., 1001)
select c.first_name, c.last_name, t.*
from transactions t
join accounts a on t.account_id = a.account_id
join customers c on a.customer_id = c.customer_id
where a.account_id = 1001;

-- 8. identify customers who have more than one account
select customer_id, count(*) as account_count
from accounts
group by customer_id
having count(*) > 1;

-- 9. calculate the difference in transaction amounts between deposits and withdrawals
select
    (select sum(amount) from transactions where transaction_type = 'deposit') -
    (select sum(amount) from transactions where transaction_type = 'withdrawal') as net_difference;

-- 10. calculate the average daily balance for each account over a specified period (simplified version)
select account_id, avg(balance) as average_balance
from accounts
group by account_id;

-- 11. calculate the total balance for each account type
select account_type, sum(balance) as total_balance
from accounts
group by account_type;

-- 12. identify accounts with the highest number of transactions in descending order
select account_id, count(*) as transaction_count
from transactions
group by account_id
order by transaction_count desc;

-- 13. list customers with high aggregate account balances along with their account types
select c.first_name, c.last_name, a.account_type, sum(a.balance) as total_balance
from customers c
join accounts a on c.customer_id = a.customer_id
group by c.first_name, c.last_name, a.account_type
having sum(a.balance) > 3000;

-- 14. identify and list duplicate transactions based on transaction amount, date, and account
select account_id, amount, cast(transaction_date as date) as txn_date, count(*)
from transactions
group by account_id, amount, cast(transaction_date as date)
having count(*) > 1;

--task 4

-- 1. retrieve the customer(s) with the highest account balance
select * from customers
where customer_id in (
    select customer_id from accounts
    where balance = (select max(balance) from accounts)
);

-- 2. calculate the average account balance for customers who have more than one account
select avg(balance) as average_balance
from accounts
where customer_id in (
    select customer_id from accounts
    group by customer_id
    having count(*) > 1
);

-- 3. retrieve accounts with transactions whose amounts exceed the average transaction amount
select * from transactions
where amount > (select avg(amount) from transactions);

-- 4. identify customers who have no recorded transactions
select * from customers
where customer_id not in (
    select customer_id from accounts
    where account_id in (select account_id from transactions)
);

-- 5. calculate the total balance of accounts with no recorded transactions
select sum(balance) as total_balance
from accounts
where account_id not in (select account_id from transactions);

-- 6. retrieve transactions for accounts with the lowest balance
select * from transactions
where account_id in (
    select account_id from accounts
    where balance = (select min(balance) from accounts)
);

-- 7. identify customers who have accounts of multiple types
select customer_id
from accounts
group by customer_id
having count(distinct account_type) > 1;

-- 8. calculate the percentage of each account type out of the total number of accounts
select account_type,
       count(*) * 100.0 / (select count(*) from accounts) as percentage
from accounts
group by account_type;

-- 9. retrieve all transactions for a customer with a given customer_id (example: 1)
select t.*
from transactions t
join accounts a on t.account_id = a.account_id
where a.customer_id = 1;

-- 10. calculate the total balance for each account type using a subquery within the select clause
select account_type,
       (select sum(balance) from accounts a2 where a2.account_type = a1.account_type) as total_balance
from accounts a1
group by account_type;






