# Student Record Management System

A console-based **Student Record Management System** developed in Java using **Advanced Object-Oriented Programming (AOOP)** concepts and file handling.

The system allows users to manage student records through a simple menu-driven interface. Student information is stored in a text file named `students.txt`.

## Features

* Insert a new student record
* Delete a student record
* Update an existing student record
* Search for a student using enrollment number
* Display all student records
* Calculate CGPI from previous semester SPI values
* Assign grades based on CGPI
* Generate performance remarks
* Store records using file handling

## Technologies Used

* Java
* Object-Oriented Programming
* File Handling
* `Scanner`
* `PrintWriter`
* `FileWriter`

## Student Information

The system stores three types of information:

### Basic Details

* Name
* Enrollment number
* Department
* Semester
* Division

### Personal Details

* Email
* Contact number
* Gender
* Date of birth
* Address

### Result Details

* Previous semester SPI
* CGPI
* Grade
* Performance remark

The project calculates CGPI from the entered SPI values and assigns a grade according to the calculated CGPI.

## Menu Options

```text
1. Insert
2. Delete
3. Update
4. Search
5. Display
6. Exit
```

## File Structure

```text
Student Record Management System/
│
├── student.java
├── students.txt
└── README.md
```

`student.java` contains the complete Java program.

`students.txt` is used to store student records when records are inserted.

## How to Run

### 1. Compile the program

Open the terminal in the project folder and run:

```bash
javac student.java
```

### 2. Run the program

```bash
java student
```

### 3. Use the menu

Choose an option from the menu and enter the required student information.

## OOP Concepts Used

This project demonstrates:

* Classes
* Objects
* Methods
* Nested classes
* Conditional statements
* Loops
* Arrays
* File handling
* Exception handling
* User input

These concepts are demonstrated in a practical student record management application.

## Project Outcome

This project provides practical experience in Java programming, Object-Oriented Programming, file handling, record management, and menu-driven console applications.

## Project Information

**Subject:** Advanced Object Oriented Programming (AOOP)

**Subject Code:** 4340701

**Project:** Student Record Management System in Java
