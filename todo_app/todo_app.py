#!/usr/bin/env python3
"""
Todo Application - Phase I: In-Memory Console-Based Todo App

This is a simple in-memory console-based todo application written in Python.
It stores data only in runtime memory and provides basic todo functionality.
"""

import json
import sys
from datetime import datetime
from typing import Dict, List, Optional


class TodoItem:
    """Represents a single todo item."""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert the todo item to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create a TodoItem from a dictionary."""
        item = cls(
            id=data['id'],
            title=data['title'],
            description=data.get('description', ''),
            completed=data.get('completed', False)
        )
        if 'created_at' in data:
            item.created_at = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            item.updated_at = datetime.fromisoformat(data['updated_at'])
        return item


class TodoManager:
    """Manages the collection of todo items in memory."""

    def __init__(self):
        self.todos: Dict[int, TodoItem] = {}
        self.next_id = 1

    def add_todo(self, title: str, description: str = "") -> TodoItem:
        """Add a new todo item."""
        if not title.strip():
            raise ValueError("Title cannot be empty")

        todo = TodoItem(self.next_id, title.strip(), description.strip())
        self.todos[self.next_id] = todo
        self.next_id += 1
        return todo

    def list_todos(self) -> List[TodoItem]:
        """Return a list of all todo items."""
        return list(self.todos.values())

    def get_todo(self, id: int) -> Optional[TodoItem]:
        """Get a specific todo item by ID."""
        return self.todos.get(id)

    def update_todo(self, id: int, title: Optional[str] = None,
                   description: Optional[str] = None,
                   completed: Optional[bool] = None) -> Optional[TodoItem]:
        """Update an existing todo item."""
        if id not in self.todos:
            return None

        todo = self.todos[id]
        if title is not None:
            todo.title = title.strip() if title else title
        if description is not None:
            todo.description = description.strip() if description else description
        if completed is not None:
            todo.completed = completed
        todo.updated_at = datetime.now()

        return todo

    def delete_todo(self, id: int) -> bool:
        """Delete a todo item by ID."""
        if id in self.todos:
            del self.todos[id]
            return True
        return False

    def toggle_completion(self, id: int) -> Optional[TodoItem]:
        """Toggle the completion status of a todo item."""
        if id not in self.todos:
            return None

        todo = self.todos[id]
        todo.completed = not todo.completed
        todo.updated_at = datetime.now()
        return todo

    def clear_all(self):
        """Clear all todo items."""
        self.todos.clear()
        self.next_id = 1


class TodoApp:
    """Main application class for the console-based todo app."""

    def __init__(self):
        self.manager = TodoManager()
        self.running = True

    def print_menu(self):
        """Print the application menu."""
        print("\n" + "="*50)
        print("TODO APPLICATION - Phase I")
        print("="*50)
        print("1. Add Todo")
        print("2. List Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Toggle Completion")
        print("6. Show Todo Details")
        print("7. Clear All Todos")
        print("8. Help")
        print("9. Exit")
        print("-"*50)

    def print_help(self):
        """Print help information."""
        print("\nHELP:")
        print("This is an in-memory console-based todo application.")
        print("All data is stored only in runtime memory.")
        print("Commands:")
        print("  add <title> [description] - Add a new todo")
        print("  list - List all todos")
        print("  update <id> [title] [description] [completed] - Update a todo")
        print("  delete <id> - Delete a todo")
        print("  toggle <id> - Toggle completion status")
        print("  show <id> - Show details of a specific todo")
        print("  clear - Clear all todos")
        print("  help - Show this help message")
        print("  exit - Exit the application")

    def print_todo_list(self):
        """Print the list of todos."""
        todos = self.manager.list_todos()

        if not todos:
            print("\nNo todos found. Add some todos!")
            return

        print(f"\n{'ID':<4} {'Title':<20} {'Description':<30} {'Status':<10}")
        print("-" * 68)

        for todo in todos:
            status = "[X] Completed" if todo.completed else "[ ] Pending"
            desc = todo.description[:27] + "..." if len(todo.description) > 27 else todo.description
            print(f"{todo.id:<4} {todo.title[:18]:<20} {desc:<30} {status:<10}")

    def print_todo_details(self, id: int):
        """Print details of a specific todo."""
        todo = self.manager.get_todo(id)
        if not todo:
            print(f"\nTodo with ID {id} not found.")
            return

        print(f"\nDetails for Todo #{todo.id}:")
        print(f"Title: {todo.title}")
        print(f"Description: {todo.description}")
        print(f"Status: {'Completed' if todo.completed else 'Pending'}")
        print(f"Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Updated: {todo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

    def handle_add(self, parts: List[str]):
        """Handle the add command."""
        if len(parts) < 2:
            print("\nUsage: add <title> [description]")
            return

        title = parts[1]
        description = " ".join(parts[2:]) if len(parts) > 2 else ""

        try:
            todo = self.manager.add_todo(title, description)
            print(f"\nAdded todo: '{todo.title}' (ID: {todo.id})")
        except ValueError as e:
            print(f"\nError: {e}")

    def handle_update(self, parts: List[str]):
        """Handle the update command."""
        if len(parts) < 2:
            print("\nUsage: update <id> [title] [description] [completed]")
            return

        try:
            id = int(parts[1])
        except ValueError:
            print("\nInvalid ID. Please provide a numeric ID.")
            return

        title = " ".join(parts[2:3]) if len(parts) > 2 else None
        description = " ".join(parts[3:4]) if len(parts) > 3 else None
        completed = parts[4].lower() == 'true' if len(parts) > 4 else None

        updated = self.manager.update_todo(id, title, description, completed)
        if updated:
            print(f"\nUpdated todo: '{updated.title}' (ID: {updated.id})")
        else:
            print(f"\nTodo with ID {id} not found.")

    def handle_delete(self, parts: List[str]):
        """Handle the delete command."""
        if len(parts) < 2:
            print("\nUsage: delete <id>")
            return

        try:
            id = int(parts[1])
        except ValueError:
            print("\nInvalid ID. Please provide a numeric ID.")
            return

        if self.manager.delete_todo(id):
            print(f"\nDeleted todo with ID {id}.")
        else:
            print(f"\nTodo with ID {id} not found.")

    def handle_toggle(self, parts: List[str]):
        """Handle the toggle command."""
        if len(parts) < 2:
            print("\nUsage: toggle <id>")
            return

        try:
            id = int(parts[1])
        except ValueError:
            print("\nInvalid ID. Please provide a numeric ID.")
            return

        todo = self.manager.toggle_completion(id)
        if todo:
            status = "completed" if todo.completed else "pending"
            print(f"\nTodo '{todo.title}' (ID: {todo.id}) marked as {status}.")
        else:
            print(f"\nTodo with ID {id} not found.")

    def handle_show(self, parts: List[str]):
        """Handle the show command."""
        if len(parts) < 2:
            print("\nUsage: show <id>")
            return

        try:
            id = int(parts[1])
        except ValueError:
            print("\nInvalid ID. Please provide a numeric ID.")
            return

        self.print_todo_details(id)

    def handle_clear(self):
        """Handle the clear command."""
        self.manager.clear_all()
        print("\nAll todos cleared.")

    def handle_command(self, command: str):
        """Handle a command from the user."""
        parts = command.lower().strip().split()

        if not parts:
            return

        cmd = parts[0]

        if cmd == 'add':
            self.handle_add(command.split())
        elif cmd == 'list':
            self.print_todo_list()
        elif cmd == 'update':
            self.handle_update(command.split())
        elif cmd == 'delete':
            self.handle_delete(command.split())
        elif cmd == 'toggle':
            self.handle_toggle(command.split())
        elif cmd == 'show':
            self.handle_show(command.split())
        elif cmd == 'clear':
            self.handle_clear()
        elif cmd == 'help':
            self.print_help()
        elif cmd == 'exit' or cmd == 'quit':
            self.running = False
        else:
            print(f"\nUnknown command: {cmd}. Type 'help' for available commands.")

    def run_interactive(self):
        """Run the interactive console application."""
        print("Welcome to the Todo Application - Phase I")
        print("Type 'help' for available commands, 'exit' to quit.")

        while self.running:
            try:
                command = input("\nEnter command: ").strip()
                self.handle_command(command)
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                self.running = False
            except EOFError:
                print("\n\nGoodbye!")
                self.running = False

    def run(self):
        """Main run method."""
        self.run_interactive()


def main():
    """Entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()