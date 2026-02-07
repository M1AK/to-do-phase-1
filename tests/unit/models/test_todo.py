"""
Unit tests for Todo model
"""

import pytest
from src.todo_app.models.todo import Todo, TodoUpdate


def test_todo_creation_valid():
    """Test creating a valid Todo object."""
    todo = Todo(id=1, title="Test todo", completed=False)

    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed is False


def test_todo_creation_with_defaults():
    """Test creating a Todo with default completed value."""
    todo = Todo(id=1, title="Test todo")

    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed is False  # Should default to False


def test_todo_id_validation_negative():
    """Test that negative ID raises ValueError."""
    with pytest.raises(ValueError, match="id must be a positive integer"):
        Todo(id=-1, title="Test todo")


def test_todo_id_validation_zero():
    """Test that zero ID raises ValueError."""
    with pytest.raises(ValueError, match="id must be a positive integer"):
        Todo(id=0, title="Test todo")


def test_todo_title_validation_empty():
    """Test that empty title raises ValueError."""
    with pytest.raises(ValueError, match="title must be a non-empty string"):
        Todo(id=1, title="")


def test_todo_title_validation_too_long():
    """Test that overly long title raises ValueError."""
    long_title = "x" * 501  # 501 characters, exceeding 500 limit
    with pytest.raises(ValueError, match="title must be a non-empty string"):
        Todo(id=1, title=long_title)


def test_todo_completed_validation_non_bool():
    """Test that non-boolean completed value raises ValueError."""
    with pytest.raises(ValueError, match="completed must be a boolean"):
        Todo.__new__.__func__(Todo, id=1, title="Test", completed="false")


def test_todo_update_creation_valid():
    """Test creating a valid TodoUpdate object."""
    update = TodoUpdate(title="New title", completed=True)

    assert update.title == "New title"
    assert update.completed is True


def test_todo_update_partial():
    """Test creating a partial TodoUpdate object."""
    update = TodoUpdate(title="New title")

    assert update.title == "New title"
    assert update.completed is None  # Should remain None


def test_todo_update_none_values():
    """Test creating a TodoUpdate with explicit None values."""
    update = TodoUpdate(title=None, completed=None)

    assert update.title is None
    assert update.completed is None


def test_todo_update_title_validation():
    """Test that invalid title in TodoUpdate raises ValueError."""
    with pytest.raises(ValueError, match="title must be a non-empty string"):
        TodoUpdate.__new__.__func__(TodoUpdate, title="", completed=None)


def test_todo_update_completed_validation():
    """Test that invalid completed in TodoUpdate raises ValueError."""
    with pytest.raises(ValueError, match="completed must be a boolean"):
        TodoUpdate.__new__.__func__(TodoUpdate, title=None, completed="true")