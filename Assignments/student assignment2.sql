--task-1--
--1. Create the database named "SISDB"
create database SISDB;
use SISDB;

create table students(
	student_id int primary key,
	first_name varchar(50),
	last_name varchar(50),
	date_of_birth date,
	email varchar(50),
	phone_number varchar(20));

create table courses (
    course_id int primary key,
    course_name varchar(100),
    credits int,
    teacher_id int,
    foreign key(teacher_id) references teacher(teacher_id));

create table enrollments(
	enrollment_id int primary key,
	student_id int,
	course_id int,
	enrollment_date date,
	foreign key(student_id) references students(student_id),
	foreign key(course_id) references courses(course_id));

create table teacher(
	teacher_id int primary key,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(50));

create table payments(
	payment_id int primary key,
	student_id int,
	amount decimal(10,2),
	payment_date date,
	foreign key(student_id) references students(student_id));

insert into students values
(1,'Nithya','sree','2004-05-06','nithya@email.com','9998887771'),
(2,'bhavya','n','2003-07-21','bhavya@email.com','9998887772'),
(3,'charan','k','2001-09-15','charan@email.com','9998887773'),
(4,'diya','sharma','2002-12-30','diya@email.com','9998887774'),
(5,'elvin','jacob','2003-04-22','elvin@email.com','9998887775'),
(6,'farah','b','2002-11-03','farah@email.com','9998887776'),
(7,'ganesh','m','2001-03-14','ganesh@email.com','9998887777'),
(8,'harsha','s','2002-08-09','harsha@email.com','9998887778'),
(9,'isha','kumar','2003-02-11','isha@email.com','9998887779'),
(10,'pavi','devi','2001-06-28','pavi@email.com','9998887780');

insert into courses values
(101, 'mathematics', 3, 1),
(102, 'physics', 4, 2),
(103, 'chemistry', 3, 3),
(104, 'biology', 3, 4),
(105, 'english', 2, 5),
(106, 'computer science', 4, 6),
(107, 'history', 2, 7),
(108, 'geography', 2, 8),
(109, 'economics', 3, 9),
(110, 'art', 1, 10);


insert into teacher values
(1, 'rajesh', 'kumar', 'rajesh@school.com'),
(2, 'sneha', 'mehta', 'sneha@school.com'),
(3, 'arun', 'joshi', 'arun@school.com'),
(4, 'meena', 'ravi', 'meena@school.com'),
(5, 'vikam', 'raja', 'vikas@school.com'),
(6, 'nisha', 'verma', 'nisha@school.com'),
(7, 'manoj', 'gupta', 'manoj@school.com'),
(8, 'priya', 'iyer', 'priya@school.com'),
(9, 'deepak', 'bose', 'deepak@school.com'),
(10, 'anita', 'paul', 'anita@school.com');

insert into enrollments values
(1, 1, 101, '2024-01-10'),
(2, 2, 102, '2024-01-11'),
(3, 3, 103, '2024-01-12'),
(4, 4, 104, '2024-01-13'),
(5, 5, 105, '2024-01-14'),
(6, 6, 106, '2024-01-15'),
(7, 7, 107, '2024-01-16'),
(8, 8, 108, '2024-01-17'),
(9, 9, 109, '2024-01-18'),
(10, 10, 110, '2024-01-19');

insert into payments values
(1, 1, 5000.00, '2024-01-20'),
(2, 2, 5200.00, '2024-01-21'),
(3, 3, 4800.00, '2024-01-22'),
(4, 4, 5100.00, '2024-01-23'),
(5, 5, 5300.00, '2024-01-24'),
(6, 6, 5500.00, '2024-01-25'),
(7, 7, 4700.00, '2024-01-26'),
(8, 8, 4900.00, '2024-01-27'),
(9, 9, 5000.00, '2024-01-28'),
(10, 10, 5400.00, '2024-01-29');

--task -3--
--1.total payments made by a specific student based on the student's ID. 
select s.first_name, s.last_name, sum(p.amount) as total_payment
from students s
join payments p on s.student_id = p.student_id
where s.student_id = 1
group by s.first_name, s.last_name;

--2. list of courses along with the count of students enrolled in each course.
-- between the "Courses" table and the "Enrollments" table.

select c.course_name,count(e.student_id)as Student_count
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_name;

--3.find the names of students who have not enrolled in any course. Use a 
--LEFT JOIN between the "Students" table and the "Enrollments" table 

select s.student_id, s.first_name, s.last_name
from students s
left join enrollments e on s.student_id = e.student_id
where e.enrollment_id is null;

--4..retrive first name, last name of students,course and join bw s,e,c

select s.first_name,s.last_name,c.course_name 
from students s
join enrollments e on s.student_id= e.student_id
join courses c on e.course_id = c.course_id;

--5. teacher,course name and join t,c

select t.first_name,t.last_name,c.course_name 
from teacher t 
join courses c on t.teacher_id= c.teacher_id;

--6. students and enrollments date for specific course ,join s,e,c

select s.first_name, s.last_name, e.enrollment_date
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
where c.course_id = 101;

--7. students with no payment,left join s,p

select s.first_name,s.last_name
from students s
left join payments p on s.student_id= p.student_id
where p.payment_id = null;

--8.course with no enrollment,left join c,e and filter enrollment with null

select c.course_id,c.course_name
from courses c
left join enrollments e on c.course_id= e.course_id
where e.enrollment_id is null;

--9.student with more than 1 course ,join on e

select s.student_id, s.first_name, s.last_name, count(e.course_id) as course_count
from students s
join enrollments e on s.student_id = e.student_id
group by s.student_id, s.first_name, s.last_name
having count(e.course_id) > 1;

--10. teacher with no course ,left join t and c is null

select t.teacher_id,first_name,t.last_name
from teacher t
left join courses c on  c.teacher_id = t.teacher_id
where c.course_id =null;

--task.4
--1.calculate avg of students in each course
--sub query
select avg(student_count) as avg_students_per_course
from (
    select count(student_id) as student_count
    from enrollments
    group by course_id) 
	as sub1;

--2.max payment made student 
select s.first_name,s.last_name,p.amount
from students s
join payments p on s.student_id = p.student_id
where p.amount=(select max(amount)from payments);

--3.list course with high enrollment
select top 1 
	c.course_name, count(e.enrollment_id) as total_enrollments
	from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_name
order by total_enrollments desc;

--4. total payment to each teacher course
select t.first_name,
(select sum(p.amount)
  from payments p
  join enrollments e on p.student_id = e.student_id
  join courses c on c.course_id = e.course_id
  where c.teacher_id = t.teacher_id) as total_payment
from teacher t;

--5. student in all courses,comp stud enroll with total no course
select s.student_id, s.first_name
from students s
where (select count(distinct e.course_id)
       from enrollments e
       where e.student_id = s.student_id) = (select count(*) from courses);

--6.teacher with no course 
select first_name
from teacher
where teacher_id not in (select teacher_id from courses);

--7. avg  age of all students--
select avg(datediff(year, date_of_birth, getdate())) as average_age
from students;

--8--course with no enrollments
select course_name
from courses
where course_id not in (select course_id from enrollments);

--9--total payment per s,course
select s.student_id, c.course_name,
  (select sum(p.amount)
   from payments p
   where p.student_id = s.student_id) as total_payment
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id;

--10--student with more than 1 payment
select student_id
from payments
group by student_id
having count(*) > 1;

--11.total payment by each student 
select s.student_id,s.first_name,sum(p.amount) as Total_payment
from students s
join payments p on s.student_id = p.student_id
group by s.student_id,s.first_name;

--12. course name with stud enrolled,join c,e
select c.course_name,count(e.student_id) as count
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_name;

--13.avg payment by student
select s.first_name,s.last_name,avg(p.amount) as avg_amount
from students s
join payments p on s.student_id= p.student_id
group by s.first_name,s.last_name;

--task--2
--1. insert into students
insert into students values (11,'john','doe','1995-08-15','doe@example.com',1234567890);

--2.enroll a student in course
insert into enrollments (enrollment_id,student_id, course_id, enrollment_date)
values (11,1, 101, '2025-04-10');

--3.update email for specific teacher
update teacher
set email='nithya1gmail.com'
where teacher_id = 3;

--4.delete enroll rec based on s,c
delete  from enrollments  where student_id =1 and course_id =1;

--5.update courses to assign teacher
update courses
set teacher_id = 1
where course_id =101;

--6.deleete spec student from enroll
delete from enrollments where student_id=1;

--7.update payment rec spec
update payments
set amount=10000.00 where payment_id =1;





