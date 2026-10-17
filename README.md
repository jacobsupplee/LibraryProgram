# Library Catalog CLI

A Python command-line library catalogue prototype for tracking available and borrowed books within a single session. Users can browse inventory, borrow a listed title, return a borrowed title, and handle invalid menu or book selections.

## Capabilities

- Display available and borrowed books
- Move a selected book between the available and borrowed collections
- Validate numeric menu and book selections
- Handle non-numeric input and empty collection states
- Keep interaction in a repeatable menu-driven workflow

## Technology

- Python 3
- Lists and collection operations
- Functions and control flow
- Exception handling
- Command-line interface

## Run locally

1. Install Python 3.
2. Clone this repository.
3. Run:

   ```bash
   python LibraryProgram.py
   ```

No third-party packages are required.

## Design notes and current limitations

This prototype uses in-memory lists, so state resets when the process ends. It does not currently include persistent storage, user accounts, due dates, or a database-backed inventory. These are reasonable extensions for a more complete library management workflow.

## Skills demonstrated

Translating a simple inventory workflow into functions, managing related collections, validating user input, and handling edge cases in an interactive CLI.

## Project context

This began as a learning project and is documented here as a software fundamentals showcase.