"""
Todo Service
Business logic layer managing todo operations
"""

from typing import List, Optional
from src.todo_app.models.todo import Todo, TodoUpdate
from src.todo_app.repositories.in_memory_repository import InMemoryTodoRepository
from src.todo_app.utils.validators import validate_todo_title, validate_todo_id


class TodoService:
    """Business logic layer managing todo operations."""

    def __init__(self, repository: InMemoryTodoRepository):
        """
        Initialize the TodoService.

        Args:
            repository: The repository to use for data access
        """
        self.repository = repository

    def add_todo(self, title: str) -> Todo:
        """
        Creates a new todo with the given title.

        Args:
            title: The title for the new todo

        Returns:
            The created Todo object
        """
        validate_todo_title(title)

        # Check for title uniqueness
        all_todos = self.repository.get_all()
        for todo in all_todos:
            if todo.title == title:
                raise ValueError(f"A todo with title '{title}' already exists")

        # Create new todo with auto-generated ID
        new_todo = Todo(id=0, title=title, completed=False)
        return self.repository.create(new_todo)

    def get_all_todos(self) -> List[Todo]:
        """
        Returns all todos.

        Returns:
            List of all Todo objects
        """
        return self.repository.get_all()

    def get_todo(self, id: int) -> Optional[Todo]:
        """
        Returns todo with specified ID or None.

        Args:
            id: The ID of the todo to retrieve

        Returns:
            Todo object if found, None otherwise
        """
        validate_todo_id(id)
        return self.repository.get_by_id(id)

    def update_todo(self, id: int, title: Optional[str] = None, completed: Optional[bool] = None) -> Optional[Todo]:
        """
        Updates todo properties.

        Args:
            id: The ID of the todo to update
            title: Optional new title
            completed: Optional new completion status

        Returns:
            Updated Todo object if successful, None if todo not found
        """
        validate_todo_id(id)

        # Get the existing todo
        existing_todo = self.repository.get_by_id(id)
        if existing_todo is None:
            return None

        # Prepare the update
        update_data = TodoUpdate(title=title, completed=completed)

        # Apply updates
        if update_data.title is not None:
            validate_todo_title(update_data.title)

            # Check for title uniqueness if changing title
            if update_data.title != existing_todo.title:
                all_todos = self.repository.get_all()
                for todo in all_todos:
                    if todo.id != id and todo.title == update_data.title:
                        raise ValueError(f"A todo with title '{update_data.title}' already exists")

            existing_todo.title = update_data.title

        if update_data.completed is not None:
            existing_todo.completed = update_data.completed

        # Save the updated todo
        return self.repository.update(id, existing_todo)

    def complete_todo(self, id: int) -> Optional[Todo]:
        """
        Marks todo as completed.

        Args:
            id: The ID of the todo to mark as completed

        Returns:
            Updated Todo object if successful, None if todo not found
        """
        validate_todo_id(id)
        return self.update_todo(id, completed=True)

    def delete_todo(self, id: int) -> bool:
        """
        Deletes todo by ID.

        Args:
            id: The ID of the todo to delete

        Returns:
            True if deleted successfully, False if todo not found
        """
        validate_todo_id(id)
        return self.repository.delete(id)

    def get_completed_todos(self) -> List[Todo]:
        """
        Returns only completed todos.

        Returns:
            List of completed Todo objects
        """
        all_todos = self.repository.get_all()
        return [todo for todo in all_todos if todo.completed]

    def get_pending_todos(self) -> List[Todo]:
        """
        Returns only pending todos.

        Returns:
            List of pending Todo objects
        """
        all_todos = self.repository.get_all()
        return [todo for todo in all_todos if not todo.completed]