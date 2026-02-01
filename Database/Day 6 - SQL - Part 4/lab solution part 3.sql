--part 3 

--1
CREATE FUNCTION dbo.GetMonthName (@InputDate DATE)
RETURNS VARCHAR(20) AS
BEGIN
    RETURN DATENAME(MONTH, @InputDate);
END;

SELECT dbo.GetMonthName('2024-12-25');

--2
CREATE FUNCTION dbo.valuerange (@Start INT, @End INT)
RETURNS @Nums TABLE (value INT)
AS
BEGIN
    WHILE @Start <= @End
    BEGIN
        INSERT INTO @Nums VALUES (@Start);
        SET @Start = @Start + 1;
    END
    RETURN;
END;

SELECT value AS Numbers
FROM dbo.valuerange(5, 8);


--3
CREATE FUNCTION dbo.GetStudentDept (@StID INT)
RETURNS TABLE
AS
RETURN
(
    SELECT 
        S.St_Fname + ' ' + S.St_Lname AS FullName,
        D.Dept_Name
    FROM Student S
    JOIN Department D ON S.Dept_Id = D.Dept_Id
    WHERE S.St_Id = @StID
);

SELECT * FROM dbo.GetStudentDept(2)



--4
CREATE FUNCTION dbo.CheckStudentName (@StID INT)
RETURNS VARCHAR(100)
AS
BEGIN
    DECLARE @Fname VARCHAR(50), @Lname VARCHAR(50);

    SELECT @Fname = St_Fname, @Lname = St_Lname
    FROM Student
    WHERE St_Id = @StID;

    IF @Fname IS NULL AND @Lname IS NULL
        RETURN 'First name & last name are null';
    ELSE IF @Fname IS NULL
        RETURN 'first name is null';
    ELSE IF @Lname IS NULL
        RETURN 'last name is null';
    
    RETURN 'First name & last name are not null';
END;

SELECT dbo.CheckStudentName(1)


CREATE FUNCTION dbo.GetManagerInfo (@MgrID INT)
RETURNS TABLE
AS
RETURN
(
SELECT D.Dept_Name, I.Ins_Name AS ManagerName,I.HireDate
FROM Instructor I 
LEFT JOIN Department D ON D.Dept_Manager = I.Ins_Id
WHERE I.Ins_Id = @MgrID 
);


--6

CREATE FUNCTION dbo.GetStudentName (@Type VARCHAR(20))
RETURNS @Result TABLE (NameValue VARCHAR(100))
AS
BEGIN
    IF LOWER(@Type) = 'first name'
        INSERT INTO @Result SELECT ISNULL(St_Fname, 'No First Name') FROM Student;

    ELSE IF LOWER(@Type) = 'last name'
        INSERT INTO @Result SELECT ISNULL(St_Lname, 'No Last Name') FROM Student;

    ELSE IF LOWER(@Type) = 'full name'
        INSERT INTO @Result 
        SELECT ISNULL(St_Fname, '') + ' ' + ISNULL(St_Lname, '') FROM Student;

    RETURN;
END;

SELECT * FROM dbo.GetStudentName('First name');
