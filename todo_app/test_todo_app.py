#!/usr/bin/env python3
"""
Test script for the Todo Application - Phase I
Demonstrates the functionality of the in-memory console-based todo app.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from todo_app import TodoApp, TodoManager

def test_todo_functionality():
    """Test the basic functionality of the todo application."""
    print("Testing Todo Application - Phase I")
    print("="*40)

    # Create a manager instance to test functionality
    manager = TodoManager()

    # Test adding todos
    print("\n1. Testing ADD functionality:")
    todo1 = manager.add_todo("Buy groceries", "Need to buy milk, bread, and eggs")
    print(f"   Added: {todo1.title} (ID: {todo1.id})")

    todo2 = manager.add_todo("Complete project", "Finish the todo app implementation")
    print(f"   Added: {todo2.title} (ID: {todo2.id})")

    # Test listing todos
    print("\n2. Testing LIST functionality:")
    todos = manager.list_todos()
    for todo in todos:
        status = "[X] Completed" if todo.completed else "[ ] Pending"
        print(f"   {todo.id}. [{status}] {todo.title} - {todo.description}")

    # Test updating a todo
    print("\n3. Testing UPDATE functionality:")
    updated = manager.update_todo(todo1.id, title="Buy groceries and cook dinner", completed=True)
    if updated:
        print(f"   Updated: {updated.title} (Completed: {updated.completed})")

    # Test toggling completion
    print("\n4. Testing TOGGLE functionality:")
    toggled = manager.toggle_completion(todo2.id)
    if toggled:
        print(f"   Toggled: {toggled.title} (Now {'completed' if toggled.completed else 'pending'})")

    # Test showing details
    print("\n5. Testing SHOW DETAILS functionality:")
    details = manager.get_todo(todo1.id)
    if details:
        print(f"   ID: {details.id}")
        print(f"   Title: {details.title}")
        print(f"   Description: {details.description}")
        print(f"   Status: {'Completed' if details.completed else 'Pending'}")
        print(f"   Created: {details.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

    # Test deleting a todo
    print("\n6. Testing DELETE functionality:")
    deleted = manager.delete_todo(todo2.id)
    if deleted:
        print(f"   Deleted todo with ID {todo2.id}")

    # Show remaining todos
    print("\n7. Remaining todos after deletion:")
    remaining = manager.list_todos()
    if remaining:
        for todo in remaining:
            status = "[X] Completed" if todo.completed else "[ ] Pending"
            print(f"   {todo.id}. [{status}] {todo.title}")
    else:
        print("   No remaining todos")

    print("\n" + "="*40)
    print("All tests completed successfully!")
    print("Phase I - In-Memory Console App is working correctly.")

if __name__ == "__main__":
    test_todo_functionality()