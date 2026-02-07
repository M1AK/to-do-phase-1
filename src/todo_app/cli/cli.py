"""
CLI Module for Todo App
Handles command-line interface and user interaction
"""

import argparse
import sys
from typing import List, Optional
from src.todo_app.services.todo_service import TodoService
from src.todo_app.repositories.in_memory_repository import InMemoryTodoRepository


class TodoCLI:
    """Command-line interface for the todo application."""

    def __init__(self):
        """Initialize the CLI with a service instance."""
        self.repository = InMemoryTodoRepository()
        self.service = TodoService(self.repository)

    def add_todo(self, title: str) -> None:
        """
        Add a new todo with the specified title.

        Args:
            title: The title for the new todo
        """
        try:
            todo = self.service.add_todo(title)
            print(f'Added todo: "{todo.title}" (ID: {todo.id})')
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def list_todos(self) -> None:
        """List all todos with their status and ID."""
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos found")
            return

        print("Todos:")
        for todo in todos:
            status = "[x]" if todo.completed else "[ ]"
            print(f"{todo.id}. {status} {todo.title}")

    def complete_todo(self, id: int) -> None:
        """
        Mark a todo as completed.

        Args:
            id: The ID of the todo to complete
        """
        try:
            todo = self.service.complete_todo(id)
            if todo:
                print(f"Todo #{id} marked as completed")
            else:
                print(f"Error: Todo #{id} not found", file=sys.stderr)
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def delete_todo(self, id: int) -> None:
        """
        Delete a todo by ID.

        Args:
            id: The ID of the todo to delete
        """
        try:
            deleted = self.service.delete_todo(id)
            if deleted:
                print(f"Todo #{id} deleted")
            else:
                print(f"Error: Todo #{id} not found", file=sys.stderr)
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def update_todo(self, id: int, new_title: str) -> None:
        """
        Update a todo's title.

        Args:
            id: The ID of the todo to update
            new_title: The new title for the todo
        """
        try:
            todo = self.service.update_todo(id, title=new_title)
            if todo:
                print(f"Todo #{id} updated")
            else:
                print(f"Error: Todo #{id} not found", file=sys.stderr)
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def show_help(self) -> None:
        """Display help information."""
        print("Todo App - Command Line Interface")
        print("")
        print("Commands:")
        print("  add <title>     Add a new todo with the specified title")
        print("  list            List all todos")
        print("  complete <id>   Mark the todo with specified ID as completed")
        print("  delete <id>     Delete the todo with specified ID")
        print("  update <id> <new_title>  Update the title of the todo with specified ID")
        print("  help            Show this help information")


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        description="Todo App - Command Line Interface",
        add_help=False
    )

    # We'll handle help ourselves
    parser.add_argument('command', nargs='?', help='Command to execute')
    parser.add_argument('args', nargs='*', help='Arguments for the command')

    return parser


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    cli = TodoCLI()

    if not hasattr(args, 'command') or args.command is None:
        print("Error: Please specify a command. Use 'help' for available commands.")
        sys.exit(2)

    command = args.command.lower()
    command_args = args.args

    if command == "add":
        if len(command_args) < 1:
            print("Error: 'add' command requires a title", file=sys.stderr)
            sys.exit(2)
        title = " ".join(command_args)
        cli.add_todo(title)

    elif command == "list":
        if len(command_args) > 0:
            print("Error: 'list' command takes no arguments", file=sys.stderr)
            sys.exit(2)
        cli.list_todos()

    elif command == "complete":
        if len(command_args) != 1:
            print("Error: 'complete' command requires an ID", file=sys.stderr)
            sys.exit(2)
        try:
            id = int(command_args[0])
            cli.complete_todo(id)
        except ValueError:
            print(f"Error: ID must be an integer, got '{command_args[0]}'", file=sys.stderr)
            sys.exit(2)

    elif command == "delete":
        if len(command_args) != 1:
            print("Error: 'delete' command requires an ID", file=sys.stderr)
            sys.exit(2)
        try:
            id = int(command_args[0])
            cli.delete_todo(id)
        except ValueError:
            print(f"Error: ID must be an integer, got '{command_args[0]}'", file=sys.stderr)
            sys.exit(2)

    elif command == "update":
        if len(command_args) < 2:
            print("Error: 'update' command requires an ID and a new title", file=sys.stderr)
            sys.exit(2)
        try:
            id = int(command_args[0])
            new_title = " ".join(command_args[1:])
            cli.update_todo(id, new_title)
        except ValueError:
            print(f"Error: ID must be an integer, got '{command_args[0]}'", file=sys.stderr)
            sys.exit(2)

    elif command == "help":
        cli.show_help()

    else:
        print(f'Error: Unknown command \'{command}\'. Use \'help\' for available commands.', file=sys.stderr)
        sys.exit(2)