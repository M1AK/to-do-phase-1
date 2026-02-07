"""
Todo Model
Represents a single todo item with essential properties for tracking tasks
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item.

    Attributes:
        id: Unique identifier for the todo item (auto-generated)
        title: Text description of the todo item (required, non-empty)
        completed: Completion status of the todo item (default: False)
    """

    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the Todo instance after initialization."""
        if self.id <= 0:
            raise ValueError(f"id must be a positive integer, got {self.id}")

        if not isinstance(self.title, str) or len(self.title) == 0 or len(self.title) > 500:
            raise ValueError(
                f"title must be a non-empty string with length 1-500 characters, "
                f"got {len(self.title)} characters"
            )

        if not isinstance(self.completed, bool):
            raise ValueError(f"completed must be a boolean, got {type(self.completed)}")


@dataclass
class TodoUpdate:
    """
    Represents updates to a Todo item.

    Attributes:
        title: Optional new title for the todo item
        completed: Optional new completion status for the todo item
    """

    title: Optional[str] = None
    completed: Optional[bool] = None

    def __post_init__(self):
        """Validate the TodoUpdate instance after initialization."""
        if self.title is not None:
            if not isinstance(self.title, str) or len(self.title) == 0 or len(self.title) > 500:
                raise ValueError(
                    f"title must be a non-empty string with length 1-500 characters, "
                    f"got {len(self.title)} characters"
                )

        if self.completed is not None and not isinstance(self.completed, bool):
            raise ValueError(f"completed must be a boolean, got {type(self.completed)}")