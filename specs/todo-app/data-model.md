# Data Model: In-Memory Python Console Todo App

## Domain Entities

### Todo Entity
**Entity Name**: Todo
**Description**: Represents a single todo item with essential properties for tracking tasks

**Fields**:
- `id` (int): Unique identifier for the todo item (auto-generated)
- `title` (str): Text description of the todo item (required, non-empty)
- `completed` (bool): Completion status of the todo item (default: False)

**Validation Rules**:
- `id`: Must be a positive integer
- `title`: Must be a non-empty string with length > 0 and <= 500 characters
- `completed`: Must be a boolean value

**State Transitions**:
- Creation: `completed` defaults to `False`
- Update: `completed` can transition from `False` to `True` or `True` to `False`
- No other state transitions allowed

## Repository Interface

### TodoRepository Protocol
**Interface Name**: TodoRepository
**Description**: Defines the contract for todo data access operations

**Methods**:
- `get_all() -> List[Todo]`: Retrieve all todos
- `get_by_id(id: int) -> Optional[Todo]`: Retrieve todo by ID, returns None if not found
- `create(todo: Todo) -> Todo`: Create a new todo and return it
- `update(id: int, todo: Todo) -> Optional[Todo]`: Update existing todo by ID, returns updated todo or None if not found
- `delete(id: int) -> bool`: Delete todo by ID, returns True if deleted, False if not found

## Service Layer Contracts

### TodoService
**Class Name**: TodoService
**Description**: Business logic layer managing todo operations

**Methods**:
- `add_todo(title: str) -> Todo`: Creates a new todo with the given title
- `get_all_todos() -> List[Todo]`: Returns all todos
- `get_todo(id: int) -> Optional[Todo]`: Returns todo with specified ID or None
- `update_todo(id: int, title: Optional[str], completed: Optional[bool]) -> Optional[Todo]`: Updates todo properties
- `complete_todo(id: int) -> Optional[Todo]`: Marks todo as completed
- `delete_todo(id: int) -> bool`: Deletes todo by ID
- `get_completed_todos() -> List[Todo]`: Returns only completed todos
- `get_pending_todos() -> List[Todo]`: Returns only pending todos

**Business Rules**:
- Todo titles must be unique (validation occurs at service level)
- Auto-generated IDs must be unique and sequential
- Cannot update a todo that doesn't exist
- Cannot mark a non-existent todo as completed

## CLI Command Contracts

### Command Format
All commands follow the format: `python main.py [action] [arguments]`

**Available Actions**:
- `add <title>`: Adds a new todo with the specified title
- `list`: Lists all todos
- `complete <id>`: Marks the todo with specified ID as completed
- `delete <id>`: Deletes the todo with specified ID
- `update <id> [title]`: Updates the title of the todo with specified ID
- `help`: Shows available commands

**Error Handling**:
- Invalid commands return appropriate error messages
- Missing arguments return usage information
- Non-existent IDs return "Todo not found" message
- Validation errors return descriptive messages