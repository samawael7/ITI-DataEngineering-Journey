--1
create view StudentGrade (fullname, course_grade)
as
	select s.St_Fname, sc.Grade 
	from Student s 
	join
	Stud_Course sc
	on s.St_Id = sc.St_Id
	where sc.Grade > 50


	select fullname, course_grade from 
	StudentGrade;


--2
create view ManagerTopics (managerName, topic)
with encryption
as
	select i.Ins_Name, t.Top_Name
	from Instructor i
	join Ins_Course ic
	on i.Ins_Id = ic.Ins_Id
	join Course c
	on ic.Crs_Id = c.Crs_Id
	join topic t
	on c.Top_Id = t.Top_Id


select * from ManagerTopics


--3
create view VInstructorSDJava
as
select i.Ins_Name, d.Dept_Name
from Instructor i
join Department d on i.Dept_Id = d.Dept_Id
where d.Dept_Name in ('SD','Java')

select * from VInstructorSDJava

--4
create view V1
as
select *
from Student
where St_Address in ('Alex','Cairo')
with check option;

Update V1 set st_address='tanta'
Where st_address='alex'

--5
use Company_SD

create view VProjectEmployees
as
select p.Pname, count(w.Essn) as EmpCount
from Project p
left join Works_For w on p.Pnumber = w.Pno
group by p.Pname;

select * from VProjectEmployees


--6
create schema Company

create schema HumanResources

alter schema company 
transfer dbo.departments


alter schema HumanResources
transfer dbo.Employee


--7
--error , already has PK
-- non clustered

create clustered index IX_HireDate
ON company.Departments(HireDate);

create nonclustered index IX_HireDate
on company.Departments(HireDate)


--8
--error duplicate ages

use ITI
CREATE UNIQUE INDEX IX_Student_UniqueAge
ON Student(St_Age);

--9
use Company_SD
declare pointer cursor
for
	select e.Salary
	from HumanResources.Employee e

for update
declare @salary int
open pointer
fetch pointer into @salary
while @@FETCH_STATUS = 0
begin
	if @salary < 3000
	update HumanResources.Employee
	set Salary = Salary * 1.1
	where current of pointer

	else if @salary >= 3000
	update 
	HumanResources.Employee
	set Salary = Salary * 1.2
	where current of pointer

	fetch pointer into @salary


end
close pointer 
deallocate pointer


--10
use ITI
declare c cursor
for
select d.Dept_Name, i.Ins_Name
from Department d join Instructor i
on d.Dept_Manager = i.Ins_Id

declare @dept varchar(50), @mgr varchar(50)

open c
fetch c into @dept, @mgr

while @@FETCH_STATUS = 0
begin
    select @dept, @mgr
    fetch c into @dept, @mgr
end

close c
deallocate c


--11
declare allnames cursor for
select St_Fname from Student

declare @name varchar(50), @result varchar(max) = ''

open allnames
fetch allnames into @name

while @@FETCH_STATUS = 0
begin
    set @result += @name + ','
    fetch allnames into @name
end

select @result

close allnames
deallocate allnames

--12

