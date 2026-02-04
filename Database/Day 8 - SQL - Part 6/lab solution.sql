--1
use ITI
create proc sp_studentcount
as
	select count(s.St_Id), d.Dept_Name
	from Student s
	join Department d
	on s.Dept_Id = d.Dept_Id
	group by d.Dept_Name


sp_studentcount


--2
use Company_SD
create proc sp_check_emp_per_project @project_no int
as
begin
	declare @count int
	select @count = count(*)
	from Works_for
	where pno = @project_no

	if @count >= 3
		select 'he number 
of employees in the project p1 is 3 or more'

	else
	begin
		select 'The following employees work for the project p1'
		select e.Fname, e.Lname
		from HumanResources.Employee e
		join Works_for w
		on e.SSN = w.ESSn
		where w.Pno = @project_no
	end
end

exec sp_check_emp_per_project 100


--3
create proc sp_oldwithnew
@old_emp int, @new_emp int, @project_num int
as
begin
	update Works_for 
	set ESSn = @new_emp
	where ESSn = @old_emp
	and pno = @project_num
end

exec sp_oldwithnew 112233, 512463, 100


--4
create table project_audit
(
    projectno int,
    username varchar(50),
    modifieddate datetime,
    budget_old int,
    budget_new int
)

alter table company.project
add budget int

update Company.Project
set budget = 50000
where budget is null;

select * from Company.Project


create trigger tr_budget_audit
on Company.project
after update
as
	declare @oldbudget int, @newbudget int
	if update(budget)
begin

	select @oldbudget = budget, pnumber from deleted
	select @newbudget = budget, pnumber from inserted

	insert into project_audit
	values(pnumber, SUSER_NAME(), GETDATE(),@oldbudget, @newbudget)

end


update Company.Project
set budget = 120000
where Pnumber = 100


--5
use ITI

create trigger tr_prevent_insert
on department
instead of insert
as
begin 
	select 'you cant insert a new record in that column'
end

insert into Department (Dept_Id, Dept_Name)
values(80,'sql');

--6
use Company_SD

create trigger tr_prevent_march
on humanResources.employee
instead of insert
as
begin
	if MONTH(GETDATE()) = 3
		select 'you cant insert in march'
	else
		insert into humanresources.employee
		select * from inserted
end


--7
use ITI
create table student_audet
(
st_username varchar(50),
audit_date datetime,
note varchar(100)
)

alter trigger tr_student_insert_audit
on student
after insert
as
begin
	insert into student_audet
	select SUSER_NAME(), GETDATE(), 
	SUSER_NAME() + 'insert new row with key= ' + cast(i.st_id as varchar) + 'in table student'

	from inserted i

end

INSERT INTO student (st_id, st_fname, st_lname) 
VALUES (277, 'sama', 'ali');


--8
create trigger trg_student_delete_audit
on student
instead of delete
as
begin
    insert into student_audet
    select
        suser_name(), getdate(),
        'try to delete row with key=' + cast(d.st_id as varchar)
    from deleted d
end

DELETE FROM student WHERE st_id = 2;
