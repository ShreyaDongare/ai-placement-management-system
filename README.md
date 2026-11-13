# AI Placement Management System

A Python-based project designed to help students manage placement-related activities. The project is being developed incrementally, starting with a command-line Student Management System.

## Project Status

**Current milestone:** Student Management System with JSON persistence.

**Completed:**
- Student registration
- View individual student details
- View all registered students
- Update student information
- Delete student records
- JSON-based data persistence
- Input validation and exception handling
- Unit testing using Python's `unittest` framework
- Nine unit tests successfully passed

## Technologies Used

- Python 3
- JSON
- pathlib
- unittest
- Git and GitHub

All current functionality uses Python's standard library. No external packages are required.

## Features

### 1. Create Student
Register a student using:
- Student ID
- Name
- Email

### 2. Read Student
- Search for a student using their ID.
- Display all registered students.

### 3. Update Student
Update a student's name or email address.

### 4. Delete Student
Delete a student using their unique student ID.

### 5. JSON Persistence
- Student records are stored in `students.json`.
- Existing records are automatically loaded when the application starts.
- Changes are saved automatically after registration, updates and deletion.
- Data remains available after restarting the application.

### 6. Error Handling
- Validate required fields.
- Prevent duplicate student IDs.
- Handle student records that do not exist.
- Handle missing JSON files.
- Detect invalid JSON data.

## Project Structure

```text
ai-placement-management-system/
│
├── main.py
├── student_manager.py
├── test_student_manager.py
├── students.json
├── README.md
└── .gitignore
```

**File descriptions:**

| File | Description |
|---|---|
| `main.py` | Command-line application and menu |
| `student_manager.py` | Student and StudentManager classes |
| `test_student_manager.py` | Unit tests |
| `students.json` | Local student data file |
| `README.md` | Project documentation |
| `.gitignore` | Files excluded from Git |

The `students.json` file is generated automatically when student data is saved. It may not exist in a fresh clone.

## Installation and Setup

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2: Open the project directory

```bash
cd ai-placement-management-system
```

### Step 3: Create a virtual environment (optional)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4: Run the application

```bash
python main.py
```

Follow the command-line menu to register, view, update and delete student records.

## Running Unit Tests

The project uses Python's built-in `unittest` framework.

Run all tests using:

```bash
python -m unittest -v
```

**Current test status:** 9 tests passed.

The test suite uses temporary directories and separate JSON files to prevent tests from modifying actual application data.

## Data Storage

Student information is stored locally in `students.json`.

Example JSON structure:

```json
[
    {
        "student_id": "101",
        "name": "Sample Student",
        "email": "student@example.com"
    },
    {
        "student_id": "102",
        "name": "Another Student",
        "email": "another@example.com"
    }
]
```

The application converts Student objects into dictionaries before writing them to JSON and recreates Student objects when loading the records.

## Git and Data Safety

The actual `students.json` file may contain personal information. Do not upload real student records to a public repository.

Add these entries to `.gitignore`:

```gitignore
# Python files
__pycache__/
*.py[cod]
.venv/

# Testing and cache
.pytest_cache/
.coverage

# Environment and sensitive data
.env
students.json
```

Never commit API keys, passwords, credentials or private student information.

## Development Workflow

Before committing changes, run the tests:

```bash
python -m unittest -v
```

Check your working tree:

```bash
git status
```

Review changes:

```bash
git diff
```

Stage only the intended files:

```bash
git add main.py student_manager.py test_student_manager.py README.md .gitignore
```

Commit your changes:

```bash
git commit -m "feat: complete student CRUD with JSON persistence"
```

Push to GitHub:

```bash
git push origin main
```

## Future Enhancements

The following features are planned for future development:

- Convert the application into a REST API using FastAPI.
- Integrate PostgreSQL and SQLAlchemy.
- Implement student authentication.
- Add admin functionality.
- Manage companies and job listings.
- Track placement applications and interview rounds.
- Develop a frontend using React and TypeScript.
- Add Docker and cloud deployment.
- Explore AI-based resume feedback and skill-to-job matching.

## Learning Outcomes

Through this project, the following concepts are being practised:

- Python OOP
- Classes and objects
- Dictionaries and lists
- Exception handling
- JSON serialization and deserialization
- File handling and pathlib
- Unit testing
- Test isolation using tempfile
- Git and GitHub workflow

## Current Development Milestone

The command-line Student Management System supports all four CRUD operations and stores student information in JSON.

The current test suite has nine passing tests.

**Next development goal:** Continue strengthening the application through additional edge-case tests and prepare the backend for future FastAPI integration.