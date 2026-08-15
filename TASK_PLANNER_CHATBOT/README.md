# Task Planner

## Description

Task Planner is a Python-based command-line application that helps users manage their tasks, deadlines, and priorities.

The application allows users to add, remove, update, and view tasks. It can also understand simple date and time inputs such as "today", "tomorrow", and specific dates and times. Tasks are automatically assigned a priority based on their deadlines, and overdue tasks are identified.

## Features

* Add new tasks
* Remove existing tasks
* Update task deadlines
* View all tasks
* Sort tasks according to deadlines
* Automatically calculate task priority
* Detect overdue tasks
* Handle duplicate tasks
* Understand simple date and time inputs
* Interactive command-line interface

## Technologies Used

* Python
* `datetime` module
* `re` (Regular Expressions)

## How It Works

The program stores each task with its title and optional deadline.

Based on the deadline:

* **High Priority** – task is overdue or due within 2 days
* **Normal Priority** – task is due within 3–7 days
* **Low Priority** – task is due after 7 days or has no deadline

The program also checks whether a task is overdue and informs the user.

## Commands

### Add a Task

```text
add submit assignment due tomorrow 5 pm
```

### Remove a Task

```text
remove submit assignment
```

### Update a Task

```text
update submit assignment
```

### Show Task List

```text
show list
```

### Exit the Program

```text
exit
```

## Example

```text
Hello! I am your Task & Time Planner.

You: add submit project due tomorrow 5 pm

Task added. See the updated list? (Yes/No)

You: yes

Your Guide Plan:
- submit project [due: 2026-08-16 17:00] (priority: high)
```

## Project Structure

```text
Task Planner/
│
├── task_planner.py
└── README.md
```

## How to Run

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python task_planner.py
```

## Author

**Riddhi Mehra**

Diploma in Computer Engineering
