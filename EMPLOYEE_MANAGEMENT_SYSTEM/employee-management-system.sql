-- 1. CREATE TABLES

CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    firstname VARCHAR(10),
    lastname VARCHAR(10),
    email VARCHAR(10) NOT NULL,
    phone INTEGER,
    hiredate DATE,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE job (
    job_id INTEGER PRIMARY KEY,
    job_title VARCHAR(25) NOT NULL,
    salary_range VARCHAR(50)
);

CREATE TABLE salary (
    salary_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    basic_salary DECIMAL(10,2),
    bonus DECIMAL(10,2),
    deductions DECIMAL(10,2),
    net_salary DECIMAL(10,2),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

-- 2. INSERT DATA

INSERT INTO department VALUES (101, 'computer engineer');
INSERT INTO department VALUES (102, 'civil engineer');
INSERT INTO department VALUES (103, 'mechanical engineer');
INSERT INTO department VALUES (104, 'graphical designer');
INSERT INTO department VALUES (105, 'architecture');

COMMIT;

-- 3. PL/SQL PROCEDURE TO CALCULATE NET SALARY

CREATE OR REPLACE PROCEDURE CalculateNetSalary(p_EmployeeID IN INT) AS
    v_BasicSalary DECIMAL(10,2);
    v_Bonus DECIMAL(10,2);
    v_Deductions DECIMAL(10,2);
    v_NetSalary DECIMAL(10,2);
BEGIN
    SELECT Basic_Salary, Bonus, Deductions
    INTO v_BasicSalary, v_Bonus, v_Deductions
    FROM Salary
    WHERE Employee_ID = p_EmployeeID;

    v_NetSalary := v_BasicSalary + v_Bonus - v_Deductions;

    DBMS_OUTPUT.PUT_LINE(
        'Net salary for employee_id ' || p_EmployeeID ||
        ' is ' || v_NetSalary
    );

    UPDATE Salary
    SET Net_Salary = v_NetSalary
    WHERE Employee_ID = p_EmployeeID;

    COMMIT;
END;

-- 4. TRIGGER TO AUTOMATICALLY CALCULATE NET SALARY

CREATE OR REPLACE TRIGGER trg_aft_salary_insert
AFTER INSERT ON Salary
FOR EACH ROW
BEGIN
    CalculateNetSalary(:NEW.Employee_ID);
END;

-- 5. QUERYING DATA USING JOIN

SELECT
    e.FirstName,
    e.LastName,
    d.Department_Name,
    j.Job_Title,
    s.Net_Salary
FROM Employee e
JOIN Department d
    ON e.Department_ID = d.Department_ID
JOIN Job j
    ON e.Job_ID = j.Job_ID
JOIN Salary s
    ON e.Employee_ID = s.Employee_ID;

-- 6. NORMALIZATION

-- First Normal Form (1NF):
-- In the employee table, each field contains only atomic values.
-- Name is split into firstname and lastname.
