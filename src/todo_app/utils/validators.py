"""
Validation utilities for the Todo App
Handles input validation and error checking
"""


def validate_todo_title(title: str) -> bool:
    """
    Validate that a todo title is acceptable.

    Args:
        title: The title to validate

    Returns:
        True if valid, raises ValueError if invalid
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string")

    if len(title) == 0:
        raise ValueError("Title cannot be empty")

    if len(title) > 500:
        raise ValueError("Title cannot exceed 500 characters")

    return True


def validate_todo_id(todo_id: int) -> bool:
    """
    Validate that a todo ID is acceptable.

    Args:
        todo_id: The ID to validate

    Returns:
        True if valid, raises ValueError if invalid
    """
    if not isinstance(todo_id, int):
        raise ValueError("ID must be an integer")

    if todo_id <= 0:
        raise ValueError("ID must be a positive integer")

    return True