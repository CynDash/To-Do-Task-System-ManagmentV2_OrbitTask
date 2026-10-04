# OrbitTask - To-Do Task Management System

## Project Description

**OrbitTask** is a desktop-based To-Do Task Management System developed using **Python and PyQt6**. It allows users to create, organize, update, complete, and delete tasks in one application.

The system is designed to help users manage their daily tasks, keep track of deadlines, organize tasks by category, and monitor their overall progress through a dashboard.

OrbitTask also identifies overdue tasks so users can easily see tasks that have passed their due date.

---

## Problem Statement

Managing tasks manually can make it difficult to remember deadlines and determine which tasks are already completed. It can also be difficult to organize different tasks and monitor overall progress.

OrbitTask addresses this problem by providing a simple desktop application where users can:

- Create and organize tasks
- Set task categories
- Set due dates
- Track completed and unfinished tasks
- Identify overdue tasks
- Monitor task progress
- Store task information using a local database

---

## Project Objectives

The main objectives of OrbitTask are:

1. To provide a simple system for creating and managing tasks.
2. To allow users to organize tasks using categories.
3. To record the created date and due date of each task.
4. To allow users to update existing tasks.
5. To allow users to delete existing tasks.
6. To allow users to mark tasks as completed.
7. To identify overdue tasks.
8. To provide separate views for In Progress, Completed, and All Tasks.
9. To provide a Dashboard that summarizes task progress.
10. To store task information using an SQLite database.
11. To demonstrate Object-Oriented Programming concepts in a practical application.

---

## Features

### 1. Dashboard

The Dashboard provides an overview of the user's tasks.

It displays:

- Total Tasks
- In Progress Tasks
- Overdue Tasks
- Completed Tasks
- Completion Progress
- Pending Tasks
- Completed Tasks

### 2. Add Task

Users can create a new task by entering:

- Task description
- Category
- Due date

The system automatically records the created date.

Available categories are:

- General
- School
- House Chores
- Work
- Personal

### 3. Update Task

Users can select an unfinished task and update its:

- Task description
- Category
- Due date

### 4. Complete Task

Users can mark an unfinished task as completed.

Completed tasks are then displayed in the **Completed** section.

### 5. Delete Task

Users can delete an existing unfinished task from the system.

The system asks for confirmation before deleting the task.

### 6. Overdue Task Detection

The system automatically identifies unfinished tasks whose due date has already passed.

These tasks are displayed with the status:

**Overdue**

### 7. Task Filtering

Users can filter tasks based on their created date.

Available date filters:

- Today
- Yesterday
- This Week
- This Month
- All Dates
- Custom Date

Users can also filter tasks by category.

### 8. Task Status

Tasks can have the following statuses:

- **In Progress** - The task has not been completed and is not overdue.
- **Completed** - The task has been marked as completed.
- **Overdue** - The task has passed its due date and has not been completed.

### 9. Task Views

The application provides four main pages:

- Dashboard
- In Progress
- Completed
- All Tasks

---

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **PyQt6** | Graphical User Interface |
| **SQLite** | Local database |
| **sqlite3** | Python library used for SQLite database operations |
| **QSS** | Application styling |
| **dataclasses** | Used for the Task model |
| **datetime** | Used for date and deadline handling |
| **pathlib** | Used for database file path management |
| **PyCharm** | Development environment |

---

## Project Structure

```text
OrbitTask/
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── features/
│   ├── __init__.py
│   └── Tasks/
│       ├── __init__.py
│       ├── model.py
│       ├── repository.py
│       ├── service.py
│       └── view.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── in-progress.png
│   ├── completed.png
│   └── all-tasks.png
│
├── Style.qss
├── main.py
├── tasks.db
└── README.md
```

### File and Folder Description

**`database/`**  
Contains the files responsible for connecting to and initializing the SQLite database.

**`database.py`**  
Creates the database connection and initializes the `tasks` table.

**`features/Tasks/`**  
Contains the main components of the task management system.

**`model.py`**  
Contains the `Task` data model. It stores task information such as ID, title, category, created date, due date, and completion status. It also determines the current status of a task.

**`repository.py`**  
Handles database operations for tasks, including adding, reading, updating, completing, and deleting tasks.

**`service.py`**  
Contains the application logic between the user interface and database repository. It also validates task information before saving it.

**`view.py`**  
Contains the graphical user interface of OrbitTask, including the Dashboard, task tables, filters, dialogs, buttons, and controls.

**`Style.qss`**  
Contains the visual styling of the application.

**`main.py`**  
The main entry point of the application. It initializes the database, creates the PyQt6 application, loads the stylesheet, creates the repository and service, and opens the main window.

**`tasks.db`**  
The local SQLite database file used to store task information.

---

## Installation and Setup

### Requirements

Before running OrbitTask, make sure you have:

- Python 3.x
- PyQt6
- PyCharm or another Python IDE (optional)

### Step 1: Clone the Repository

Clone the project from GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Then open the project folder.

### Step 2: Install PyQt6

Open the terminal inside the project folder and run:

```bash
pip install PyQt6
```

### Step 3: Check the Project Structure

Make sure the project contains:

```text
main.py
Style.qss
database/
features/
screenshots/
```

### Step 4: Run the Application

Run:

```bash
python main.py
```

If you are using PyCharm, open `main.py` and click the **Run** button.

### Step 5: Database Initialization

The SQLite database is initialized automatically when the application starts.

The database file is:

```text
tasks.db
```

---

## How to Use the System

### 1. Open OrbitTask

Run:

```bash
python main.py
```

The OrbitTask window will open.

### 2. Add a Task

1. Go to the **In Progress** page.
2. Click **+ Add Task**.
3. Enter the task description.
4. Select a category.
5. Select a due date.
6. Click **Save**.
7. The task will be added to the database and displayed in the task list.

### 3. Update a Task

1. Go to the **In Progress** page.
2. Select a task.
3. Click **Update**.
4. Change the task information.
5. Click **Save**.

### 4. Complete a Task

1. Go to the **In Progress** page.
2. Select an unfinished task.
3. Click **Complete**.
4. The task will be marked as **Completed**.
5. The task will appear in the Completed section.

### 5. Delete a Task

1. Go to the **In Progress** page.
2. Select a task.
3. Click **Delete**.
4. Confirm the deletion.
5. The task will be removed from the database.

### 6. Filter Tasks

Use the filter controls at the top of the application.

You can filter tasks by:

- Date
- Category

For dates, you can select:

- Today
- Yesterday
- This Week
- This Month
- All Dates
- Custom Date

---

## OOP Implementation

OrbitTask uses Object-Oriented Programming through several classes.

### Important Classes

#### `Task`

Located in:

```text
features/Tasks/model.py
```

The `Task` class represents a task in the system.

It contains:

```text
id
title
category
created_date
due_date
is_completed
```

It also contains a `status` property that determines whether a task is:

- In Progress
- Completed
- Overdue

#### `TaskRepository`

Located in:

```text
features/Tasks/repository.py
```

The `TaskRepository` class handles communication with the SQLite database.

Important methods include:

```text
add_task()
get_tasks_by_date()
get_all_tasks()
update_task()
complete_task()
delete_task()
```

#### `TaskService`

Located in:

```text
features/Tasks/service.py
```

The `TaskService` class handles application logic and validation between the user interface and repository.

#### `TaskDialog`

Located in:

```text
features/Tasks/view.py
```

`TaskDialog` is used for adding and updating tasks.

It inherits from the PyQt6 `QDialog` class.

#### `TaskView`

Located in:

```text
features/Tasks/view.py
```

`TaskView` is the main application window.

It inherits from the PyQt6 `QMainWindow` class.

---

## OOP Concepts Used

OrbitTask uses Object-Oriented Programming (OOP) through the use of classes, objects, encapsulation, inheritance, and polymorphism.

### Encapsulation

Encapsulation is demonstrated by grouping related data and behavior inside classes.

For example, the `Task` class contains information about a task such as:

- `id`
- `title`
- `category`
- `created_date`
- `due_date`
- `is_completed`

It also contains the `status` property that determines the current status of the task.

The other classes have their own responsibilities:

- `TaskRepository` handles database operations.
- `TaskService` handles application logic and validation.
- `TaskView` handles the graphical user interface.

### Inheritance

Inheritance is used with PyQt6 classes.

For example:

```python
class TaskDialog(QDialog):
```

The `TaskDialog` class inherits from `QDialog`, allowing it to use the features and behavior provided by the PyQt6 dialog class.

Another example is:

```python
class TaskView(QMainWindow):
```

The `TaskView` class inherits from `QMainWindow`, allowing it to use the features provided by the PyQt6 main window class.

### Polymorphism

Polymorphism is demonstrated through the use of PyQt6's inherited classes and their methods.

The custom classes `TaskDialog` and `TaskView` use the interfaces and behavior provided by their respective Qt parent classes while implementing the functionality needed by OrbitTask.

This allows the application to use common Qt methods while providing application-specific behavior in the custom classes.

---

## Database

OrbitTask uses **SQLite** for local data storage.

The database file is:

```text
tasks.db
```

### Database Table

The main database table is:

### `tasks`

| Field | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique task ID |
| `title` | TEXT | Task description |
| `category` | TEXT | Task category |
| `created_date` | TEXT | Date the task was created |
| `due_date` | TEXT | Task deadline |
| `is_completed` | INTEGER | Completion status |

The `is_completed` field uses:

```text
0 = Not Completed
1 = Completed
```

### Database Operations

**Create** - A new task is inserted into the `tasks` table.

**Read** - The system retrieves tasks from the database.

**Update** - Existing task information can be updated.

**Delete** - A selected task can be removed from the database.

**Complete** - A task can be marked as completed by changing `is_completed` to `1`.

---

## Screenshots

### Dashboard

The Dashboard displays the overall task information, including total tasks, in-progress tasks, overdue tasks, completed tasks, completion progress, and task lists.

![Dashboard](screenshots/dashboard.png)

### In Progress

The In Progress page displays unfinished tasks and provides the main task management buttons.

![In Progress](screenshots/in-progress.png)

### Completed

The Completed page displays tasks that have already been marked as completed.

![Completed](screenshots/completed.png)

### All Tasks

The All Tasks page displays all stored tasks, including their category, created date, due date, and current status.

![All Tasks](screenshots/all-tasks.png)

---

## Testing

The system was tested by performing the main task management operations.

| Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|
| Add a new task | New task should appear in the task list | Task was added successfully | Passed |
| Update a task | Selected task information should be updated | Task information was updated | Passed |
| Complete a task | Task status should change to Completed | Task was marked as Completed | Passed |
| Delete a task | Selected task should be removed | Task was deleted successfully | Passed |
| View In Progress | Unfinished tasks should be displayed | Tasks were displayed correctly | Passed |
| View Completed | Completed tasks should be displayed | Tasks were displayed correctly | Passed |
| View All Tasks | All stored tasks should be displayed | Tasks were displayed correctly | Passed |
| Detect overdue tasks | Past-due unfinished tasks should show Overdue | Overdue tasks were identified | Passed |
| Filter by date | Matching tasks should be displayed | Date filtering worked | Passed |
| Filter by category | Matching category tasks should be displayed | Category filtering worked | Passed |

---

## Known Issues / Limitations

The current version of OrbitTask has the following limitations:

1. The application is designed for a single local user.
2. The database is stored locally using SQLite.
3. There is no online or cloud synchronization.
4. There is no user login or account system.
5. There are no email or mobile notifications.
6. Task categories are limited to the categories provided by the application.
7. The system does not have a cloud database.
8. Task management actions such as Update, Complete, and Delete are currently intended for unfinished tasks on the **In Progress** page.
9. The system does not currently include a dedicated search feature.
10. The application focuses on basic task management rather than advanced project management.

---

## Author

**Name:** Cyril John Dragas  
**Section:** CS26L - 3581
