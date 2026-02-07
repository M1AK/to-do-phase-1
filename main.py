#!/usr/bin/env python3
"""
Todo App - Main Entry Point
Command-line interface for managing todo items
"""

import sys
from src.todo_app.cli.cli import main as cli_main


def main():
    """Main entry point for the todo application."""
    cli_main()


if __name__ == "__main__":
    main()