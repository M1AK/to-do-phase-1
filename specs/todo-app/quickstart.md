# Quickstart Guide: In-Memory Python Console Todo App

## Setup Instructions

### Prerequisites
- Python 3.13+ installed
- UV package manager installed (optional, for dependency management)

### Installation Steps

1. **Clone or create the project structure**:
```bash
mkdir todo-app
cd todo-app
```

2. **Create the directory structure**:
```bash
mkdir -p src/todo_app/{models,repositories,services,cli,utils}
mkdir -p tests/{unit,integration,contract}
```

3. **Create the main entry point** (`main.py`):
```bash
touch main.py
```

4. **Initialize the package files**:
```bash
touch src/todo_app/__init__.py
touch src/todo_app/models/__init__.py
touch src/todo_app/repositories/__init__.py
touch src/todo_app/services/__init__.py
touch src/todo_app/cli/__init__.py
touch src/todo_app/utils/__init__.py
```

## Running the Application

### Direct Execution
```bash
python main.py [command] [arguments]
```

### Available Commands
- `python main.py add "Buy groceries"` - Add a new todo
- `python main.py list` - List all todos
- `python main.py complete 1` - Mark todo #1 as completed
- `python main.py delete 1` - Delete todo #1
- `python main.py update 1 "Updated title"` - Update todo #1's title
- `python main.py help` - Show help information

### Example Usage Session
```bash
$ python main.py add "Learn Python"
Added todo: "Learn Python" (ID: 1)

$ python main.py add "Build a todo app"
Added todo: "Build a todo app" (ID: 2)

$ python main.py list
Todos:
1. [ ] Learn Python
2. [ ] Build a todo app

$ python main.py complete 1
Todo #1 marked as completed

$ python main.py list
Todos:
1. [x] Learn Python
2. [ ] Build a todo app

$ python main.py delete 2
Todo #2 deleted
```

## Development Setup

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test files
python -m pytest tests/unit/
python -m pytest tests/integration/
```

### Project Structure Reference
```
todo-app/
├── main.py                 # Entry point with CLI loop
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── todo.py     # Todo data model
│       ├── repositories/
│       │   ├── __init__.py
│       │   └── in_memory_repository.py  # In-memory storage
│       ├── services/
│       │   ├── __init__.py
│       │   └── todo_service.py         # Business logic
│       ├── cli/
│       │   ├── __init__.py
│       │   └── cli.py      # Command parsing and output
│       └── utils/
│           ├── __init__.py
│           └── validators.py # Input validation
├── tests/
│   ├── unit/               # Unit tests for individual components
│   ├── integration/        # Integration tests for CLI flow
│   └── contract/           # Contract tests for API stability
└── pyproject.toml          # Project configuration
```

## Configuration

### Environment Variables (if any)
The application uses only in-memory storage and has no external configuration requirements. All state is maintained during the application runtime.

### Dependencies
The application uses only Python standard library components:
- `argparse` for command-line parsing
- `dataclasses` for data modeling
- `typing` for type hints
- `sys` and `os` for system operations