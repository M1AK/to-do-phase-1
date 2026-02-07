# Todo Application - Phase I

This is the first phase of our progressive AI-native todo application. It's an in-memory console-based todo app built with Python.

## Features

- Add, list, update, delete, and toggle completion status of todos
- All data stored in runtime memory (no persistence)
- Console-based command interface
- Single-user execution

## Commands

- `add <title> [description]` - Add a new todo
- `list` - List all todos
- `update <id> [title] [description] [completed]` - Update a todo
- `delete <id>` - Delete a todo
- `toggle <id>` - Toggle completion status
- `show <id>` - Show details of a specific todo
- `clear` - Clear all todos
- `help` - Show help information
- `exit` - Exit the application

## Running the Application

```bash
python todo_app.py
```

Or run interactively:

```bash
cd todo_app
python todo_app.py
```

## Architecture

This phase implements the core todo functionality in memory with:

- `TodoItem` class: Represents individual todo items
- `TodoManager` class: Manages the collection of todo items
- `TodoApp` class: Main application with console interface

## Limitations

- Data is stored only in runtime memory (lost when program exits)
- Single-user execution
- No external persistence
- Console-based interface only

## Next Phases

- Phase II: Full-Stack Web Application with Next.js, FastAPI, SQLModel, and Neon PostgreSQL
- Phase III: AI-Powered Todo Chatbot with OpenAI integration
- Phase IV: Local Kubernetes Deployment with Docker and Minikube
- Phase V: Advanced Cloud Deployment with Kafka and Dapr