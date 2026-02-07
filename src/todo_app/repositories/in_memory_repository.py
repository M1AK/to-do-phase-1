"""
In-Memory Repository for Todo Items
Provides data access operations using list-based storage
"""

from typing import List, Optional
from src.todo_app.models.todo import Todo


class TodoRepository:
    """Protocol defining the contract for todo data access operations."""

    def get_all(self) -> List[Todo]:
        """Retrieve all todos."""
        raise NotImplementedError

    def get_by_id(self, id: int) -> Optional[Todo]:
        """Retrieve todo by ID, returns None if not found."""
        raise NotImplementedError

    def create(self, todo: Todo) -> Todo:
        """Create a new todo and return it."""
        raise NotImplementedError

    def update(self, id: int, todo: Todo) -> Optional[Todo]:
        """Update existing todo by ID, returns updated todo or None if not found."""
        raise NotImplementedError

    def delete(self, id: int) -> bool:
        """Delete todo by ID, returns True if deleted, False if not found."""
        raise NotImplementedError


class InMemoryTodoRepository(TodoRepository):
    """In-memory implementation of TodoRepository using list-based storage."""

    def __init__(self):
        """Initialize the in-memory repository."""
        self._todos: List[Todo] = []
        self._next_id = 1

    def get_all(self) -> List[Todo]:
        """Retrieve all todos."""
        # Return a copy to prevent external modification
        return [todo for todo in self._todos]

    def get_by_id(self, id: int) -> Optional[Todo]:
        """Retrieve todo by ID, returns None if not found."""
        for todo in self._todos:
            if todo.id == id:
                return todo
        return None

    def create(self, todo: Todo) -> Todo:
        """Create a new todo and return it."""
        # Assign an ID if not provided or if it's the default placeholder
        if todo.id <= 0:
            todo.id = self._next_id
            self._next_id += 1
        elif todo.id >= self._next_id:
            self._next_id = todo.id + 1

        self._todos.append(todo)
        return todo

    def update(self, id: int, todo: Todo) -> Optional[Todo]:
        """Update existing todo by ID, returns updated todo or None if not found."""
        for i, existing_todo in enumerate(self._todos):
            if existing_todo.id == id:
                # Preserve the ID from the original
                todo.id = existing_todo.id
                self._todos[i] = todo
                return todo
        return None

    def delete(self, id: int) -> bool:
        """Delete todo by ID, returns True if deleted, False if not found."""
        for i, todo in enumerate(self._todos):
            if todo.id == id:
                del self._todos[i]
                return True
        return False

    def clear(self):
        """Clear all todos from the repository."""
        self._todos.clear()
        self._next_id = 1