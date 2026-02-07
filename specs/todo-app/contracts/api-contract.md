# API Contract: Todo Console Application

## Command Line Interface Specification

### Commands Overview

| Command | Arguments | Description | Expected Output |
|---------|-----------|-------------|-----------------|
| `add` | `<title>` | Add a new todo item | Success: "Added todo: \"[title]\" (ID: [id])"<br>Error: "Error: Title cannot be empty" |
| `list` | none | List all todo items | Success: Formatted list of all todos<br>Error: "No todos found" |
| `complete` | `<id>` | Mark todo as completed | Success: "Todo #[id] marked as completed"<br>Error: "Error: Todo #[id] not found" |
| `delete` | `<id>` | Delete a todo item | Success: "Todo #[id] deleted"<br>Error: "Error: Todo #[id] not found" |
| `update` | `<id> <new_title>` | Update todo title | Success: "Todo #[id] updated"<br>Error: "Error: Todo #[id] not found" |
| `help` | none | Show help information | Help text with available commands |

### Response Format

#### Success Responses
- **Format**: Plain text messages to stdout
- **Examples**:
  - `"Added todo: \"Sample task\" (ID: 1)"`
  - `"Todos:\n1. [ ] Sample task\n2. [x] Completed task"`

#### Error Responses
- **Format**: Error messages prefixed with "Error: " to stderr
- **Examples**:
  - `"Error: Todo #5 not found"`
  - `"Error: Title cannot be empty"`

### Data Model Contract

#### Todo Representation
```
{
  "id": int,
  "title": string,
  "completed": bool
}
```

#### Validation Rules
- `id`: Positive integer (1, 2, 3...)
- `title`: String between 1-500 characters, non-empty
- `completed`: Boolean value (true/false)

### Error Codes Mapping

| Error Type | Code | Message Template |
|------------|------|------------------|
| NotFound | 404 | "Error: Todo #[id] not found" |
| ValidationError | 400 | "Error: [specific validation error]" |
| InvalidCommand | 400 | "Error: Unknown command '[command]'. Use 'help' for available commands." |

### Exit Codes
- `0`: Successful execution
- `1`: General error
- `2`: Command-line parsing error

### Examples

#### Adding a Todo
```
Input: python main.py add "Buy milk"
Output: Added todo: "Buy milk" (ID: 1)
Exit Code: 0
```

#### Listing Todos
```
Input: python main.py list
Output: Todos:
        1. [ ] Buy milk
        2. [x] Pay bills
Exit Code: 0
```

#### Completing a Todo
```
Input: python main.py complete 1
Output: Todo #1 marked as completed
Exit Code: 0
```

#### Error Case
```
Input: python main.py complete 99
Output: Error: Todo #99 not found
Exit Code: 1
```