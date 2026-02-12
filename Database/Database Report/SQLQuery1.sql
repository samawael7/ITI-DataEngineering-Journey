create database DatabaseTask

use DatabaseTask;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name NVARCHAR(50),
    CourseID INT,
    EnrollmentDate DATE
);

INSERT INTO Students VALUES
(1, 'Alice', 101, '2026-01-10'),
(2, 'Bob', 102, '2026-01-12'),
(3, 'Charlie', 101, '2026-01-15'),
(4, 'Diana', 103, '2026-01-18');

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName NVARCHAR(50),
    Instructor NVARCHAR(50)
);

INSERT INTO Courses VALUES
(101, 'SQL Basics', 'Eng Shimaa'),
(102, 'Data Warehousing', 'Eng Omar'),
(103, 'Python Programming', 'Eng Sarah');

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Grade DECIMAL(4,2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Enrollments VALUES
(1, 1, 101, 85),
(2, 2, 102, 90),
(3, 3, 101, 78),
(4, 4, 103, 88);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    StudentID INT,
    Amount DECIMAL(10,2),
    PaymentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

INSERT INTO Payments VALUES
(1, 1, 500, '2026-01-15'),
(2, 2, 700, '2026-01-16'),
(3, 3, 450, '2026-01-17'),
(4, 4, 600, '2026-01-18');



CREATE SYNONYM Std FOR Students;

SELECT * FROM Std;

SELECT 
    CourseID,
    StudentID,
    Grade,
    RANK() OVER (PARTITION BY CourseID ORDER BY Grade DESC) AS RankInCourse
FROM Enrollments;


SELECT CourseID, SUM(Grade) AS TotalGrade
FROM Enrollments
GROUP BY ROLLUP(CourseID)


SELECT CourseID, StudentID, SUM(Grade) AS TotalGrade
FROM Enrollments
GROUP BY CUBE(CourseID, StudentID);


SELECT CourseID, StudentID, SUM(Grade) AS TotalGrade
FROM Enrollments
GROUP BY GROUPING SETS(
    (CourseID),
    (StudentID),
    ()
);


SELECT *
FROM (
    SELECT CourseID, StudentID, Grade
    FROM Enrollments
) AS SourceTable
PIVOT (
    AVG(Grade)
    FOR CourseID IN ([101], [102], [103])
) AS PivotResult;



CREATE TABLE #TempStudents (
    StudentID INT,
    Name NVARCHAR(50)
);

INSERT INTO #TempStudents
SELECT StudentID, Name FROM Students;

SELECT * FROM #TempStudents;


CREATE TABLE ##GlobalStudents (
    StudentID INT,
    Name NVARCHAR(50)
);

INSERT INTO ##GlobalStudents
SELECT StudentID, Name FROM Students;

SELECT * FROM ##GlobalStudents;


BACKUP DATABASE DatabaseTask
TO DISK = 'D:\ITI Data Engineering\ITI - DataEngineering - journey\Database\Database Report\DatabaseTask_Full.bak'
WITH FORMAT,
NAME = 'Full Backup of DatabaseTask';

BACKUP DATABASE DatabaseTask
TO DISK = 'D:\ITI Data Engineering\ITI - DataEngineering - journey\Database\Database Report\DatabaseTask_Diff.bak'
WITH DIFFERENTIAL,
NAME = 'Differential Backup of DatabaseTask'

BACKUP LOG DatabaseTask
TO DISK = 'D:\ITI Data Engineering\ITI - DataEngineering - journey\Database\Database Report\DatabaseTask_Log.trn'
WITH NAME = 'Transaction Log Backup of DatabaseTask';