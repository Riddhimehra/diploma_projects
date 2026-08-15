# Employee Management System

## Project Overview

The Employee Management System is an RDBMS microproject developed using Oracle SQL and PL/SQL. It is designed to manage employee information such as personal details, departments, job roles, and salaries.

## Topics Covered

* DBMS and SQL Commands
* Normalization
* PL/SQL
* Triggers
* Primary and Foreign Keys
* JOIN Queries

## Database Tables

The project contains the following tables:

* **Employee** – Stores employee personal and department information.
* **Department** – Stores department details.
* **Job** – Stores job titles and salary ranges.
* **Salary** – Stores basic salary, bonus, deductions, and net salary.

## Main Features

* Creation and management of relational database tables.
* Insertion of employee, department, job, and salary data.
* Use of primary keys and foreign keys.
* Calculation of net salary using a PL/SQL procedure.
* Automatic salary calculation using a database trigger.
* Retrieving employee information using JOIN queries.
* Demonstration of First Normal Form (1NF).

## Technologies Used

* Oracle SQL
* PL/SQL
* RDBMS

## Net Salary Calculation

The project calculates net salary using:

**Net Salary = Basic Salary + Bonus - Deductions**

A PL/SQL procedure named `CalculateNetSalary` performs the calculation and updates the Salary table. A trigger automatically calls the procedure after a salary record is inserted.

## Conclusion

This project demonstrates the use of relational database concepts, SQL, PL/SQL, normalization, triggers, and JOIN queries to manage employee data efficiently.
