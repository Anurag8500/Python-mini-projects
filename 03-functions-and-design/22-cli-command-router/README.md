# Project #22: CLI Command Router

A Python-based command-line task manager that replaces a traditional numbered menu with a command-driven interface.

This project is part of **Phase 03 — Functions & Program Design** and focuses on command parsing, function dispatch, arguments, reusable functions, and dictionary-based command routing.

Instead of selecting numbered options, users interact with the application by entering commands such as:

```text
> add Learn Python functions | high
> list
> complete 2
> search python
> stats
```

## Features

* Command-driven terminal interface
* Add tasks
* List tasks
* Filter tasks by status
* Filter tasks by priority
* Show individual tasks
* Complete tasks
* Reopen completed tasks
* Delete tasks
* Search tasks by keyword
* Clear completed tasks
* Display task statistics
* Built-in command help
* Command-specific usage information
* Dictionary-based command routing
* Shared command argument handling

## Concepts Practiced

### Functions

* Function definitions
* Function calls
* Parameters
* Arguments
* Return values
* Helper functions
* Reusable functions
* Functions passed as values
* Function composition
* Single-responsibility functions

### Command-Line Programming

* Command parsing
* Command arguments
* Command dispatch
* Command routing
* Interactive command loops
* Unknown-command handling

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Dictionary `.get()`
* Dictionary `.items()`

### Data Processing

* `len()`
* `sum()`
* `sorted()`
* List comprehensions
* Generator expressions
* Dictionary counting
* String splitting

### String Processing

* `.strip()`
* `.lower()`
* `.split()`
* `maxsplit`

### Validation

* Numeric ID validation
* Empty input validation
* Priority validation
* Command validation

## Why This Project Exists

Previous projects used a traditional numbered menu:

```text
1. Add
2. View
3. Delete
4. Search
```

That approach is useful for beginners, but real command-line applications often allow users to enter commands directly.

Project #22 introduces this model:

```text
> add Learn Python | high
> list
> complete 3
> search Python
> stats
```

The program must therefore understand:

```text
Command
+
Arguments
```

and route the command to the appropriate function.

## Main Commands

```text
add <title> | <priority>
list [filter]
show <id>
complete <id>
reopen <id>
delete <id>
search <keyword>
stats
clear-completed
help
info <command>
exit
```

## Example Session

```text
=== CLI Command Router ===

Type 'help' to see available commands.

> list

=== Tasks ===
[1] Learn Python functions | Priority: High | Status: Pending
[2] Build mini project | Priority: Medium | Status: Pending
[3] Read Python documentation | Priority: Low | Status: Completed

> complete 1

Task 1 marked as completed.

> search python

=== Search Results ===
[1] Learn Python functions | Priority: High | Status: Completed

> stats

=== Task Statistics ===

Total tasks: 3
Pending tasks: 1
Completed tasks: 2

Tasks by priority:
- High: 1
- Low: 1
- Medium: 1
```

## Command Parsing

The program receives the complete command as one string.

For example:

```text
> search python
```

The input is split into two parts:

```python
parts = command_line.split(maxsplit=1)
```

Result:

```python
[
    "search",
    "python"
]
```

The first item is the command:

```python
command_name = parts[0].lower()
```

The second item becomes the command arguments:

```python
arguments = parts[1]
```

Conceptually:

```text
search python
   ↓
command      → search
arguments    → python
```

## Why `maxsplit=1`?

The program uses:

```python
command_line.split(maxsplit=1)
```

instead of simply:

```python
command_line.split()
```

because the remaining text should stay together as the argument.

For example:

```text
search python functions
```

becomes:

```python
[
    "search",
    "python functions"
]
```

instead of:

```python
[
    "search",
    "python",
    "functions"
]
```

This is important when an argument can contain spaces.

## Command Routing

The central design of the project is the command dictionary:

```python
commands = {
    "add": add_task,
    "list": list_tasks,
    "show": show_task,
    "complete": complete_task,
    "reopen": reopen_task,
    "delete": delete_task,
    "search": search_tasks,
    "stats": show_stats,
    "clear-completed": clear_completed,
    "help": show_help,
    "info": show_command_info
}
```

The dictionary maps command names to functions.

For example:

```text
"search"
    ↓
search_tasks
```

and:

```text
"stats"
    ↓
show_stats
```

## Functions as Values

Python functions can be stored in variables and data structures.

For example:

```python
commands = {
    "search": search_tasks
}
```

Here, `search_tasks` is being stored as a value.

The function is not executed when the dictionary is created.

The function is executed later:

```python
command_function(arguments)
```

This is the foundation of the command-routing system.

## Dynamic Dispatch

The router retrieves the correct function dynamically:

```python
command_function = commands.get(
    command_name
)
```

For:

```text
> search python
```

the lookup becomes conceptually:

```python
command_function = commands.get("search")
```

which returns:

```python
search_tasks
```

The router can then call:

```python
command_function("python")
```

This means the router does not need a large chain of:

```python
if command_name == "add":
    ...
elif command_name == "list":
    ...
elif command_name == "search":
    ...
```

The command dictionary handles the dispatch.

## Command Arguments

Every command function receives an `arguments` parameter.

For example:

```python
def complete_task(arguments):
```

When the user enters:

```text
> complete 3
```

the router passes:

```text
"3"
```

to the function.

The function is then responsible for interpreting its argument.

This creates a simple interface:

```text
Router
  ↓
command name
  ↓
function
  ↓
arguments
```

## Adding Tasks

Tasks can be created using:

```text
> add Learn Python functions | high
```

The program separates the title and priority using:

```python
parts = arguments.split("|")
```

The result is conceptually:

```python
[
    "Learn Python functions ",
    " high"
]
```

The values are then cleaned using `.strip()`.

If no priority is provided, the application defaults to:

```text
medium
```

Example:

```text
> add Study dictionaries
```

creates a medium-priority task.

## Listing Tasks

The `list` command displays all tasks:

```text
> list
```

Optional filters are also supported:

```text
> list pending
> list completed
> list high
> list medium
> list low
```

The command therefore behaves differently depending on its arguments.

## Completing Tasks

A task can be completed with:

```text
> complete 2
```

The task's state changes from:

```text
pending
```

to:

```text
completed
```

The project therefore continues the state-management concept introduced in earlier projects.

## Reopening Tasks

Completed tasks can be moved back to the pending state:

```text
> reopen 2
```

The state transitions from:

```text
completed
    ↓
pending
```

## Deleting Tasks

Tasks can be deleted using their ID:

```text
> delete 3
```

The program first finds the task and then removes it from the list.

## Searching

The search command accepts a keyword:

```text
> search python
```

The program checks whether the keyword occurs inside each task title.

Searching is case-insensitive.

For example:

```text
> search PYTHON
```

and:

```text
> search python
```

produce the same matching results.

## Task Statistics

The `stats` command calculates:

* Total tasks
* Pending tasks
* Completed tasks
* Tasks grouped by priority

Example:

```text
=== Task Statistics ===

Total tasks: 3
Pending tasks: 2
Completed tasks: 1

Tasks by priority:
- High: 1
- Low: 1
- Medium: 1
```

This reuses the aggregation patterns from previous projects.

## Clearing Completed Tasks

The command:

```text
> clear-completed
```

finds all completed tasks and removes them.

The number of deleted tasks is then displayed.

This demonstrates how a command can perform an operation on an entire subset of records.

## Help System

The `help` command displays available commands:

```text
> help
```

The application also supports command-specific information:

```text
> info search
```

which displays:

```text
Usage: search <keyword>
```

This demonstrates how a command system can provide its own interface documentation.

## Unknown Commands

When the user enters a command that is not registered:

```text
> something
```

the router detects that no matching function exists.

The program responds with:

```text
Unknown command: 'something'
Type 'help' to see available commands.
```

This prevents invalid commands from terminating the application.

## Command Router Architecture

The application's flow can be summarized as:

```text
User input
    ↓
Parse command line
    ↓
Extract command name + arguments
    ↓
Look up command in dictionary
    ↓
Retrieve function
    ↓
Call function(arguments)
    ↓
Execute requested operation
```

This architecture is the central lesson of the project.

## Traditional Menu vs Command Router

### Traditional menu

```text
1. Add
2. List
3. Search
4. Delete
```

The program usually requires the user to select a numeric option.

### Command router

```text
> add Learn Python | high
> list
> search python
> delete 2
```

The user directly describes the operation.

The router then determines which function should execute.

## Project Structure

```text
22-cli-command-router/
│
├── main.py
└── README.md
```

The project remains in a single file intentionally.

The focus is on understanding **functions as values, command parsing, and dispatch**, rather than introducing multiple modules too early.

## How to Run

From the project directory:

```bash
python main.py
```

After starting the application:

```text
> help
```

will display the available commands.

## Example Workflow

```text
Start application
      ↓
Run `help`
      ↓
Add tasks
      ↓
List / filter tasks
      ↓
Search tasks
      ↓
Complete or reopen tasks
      ↓
View statistics
      ↓
Clear completed tasks
      ↓
Exit
```

## Learning Progression

Project #22 builds on the function-design work from Projects #18–#21:

```text
Project #18
Functions + modular program structure
        ↓
Project #19
Reusable validation functions
        ↓
Project #20
Function composition + text utilities
        ↓
Project #21
Filesystem functions
        ↓
Project #22
Command parsing + function dispatch
```

The important progression is:

```text
Functions
    ↓
Reusable functions
    ↓
Functions working together
    ↓
Functions interacting with external systems
    ↓
Functions selected dynamically at runtime
```

## Why This Project Matters

Command routing is a useful pattern for CLI applications and larger software systems.

The same general idea appears when applications map:

```text
Command / Action
      ↓
Handler
      ↓
Operation
```

Examples include:

```text
CLI commands
HTTP routes
Event handlers
Plugin systems
Command systems
Task dispatchers
```

The project therefore introduces a design pattern that will become useful in later Python tooling and backend projects.

## Future Improvements

Possible extensions include:

* Support command aliases
* Add command history
* Add persistent task storage
* Add more command argument parsing
* Support quoted arguments
* Add subcommands
* Add command validation functions
* Move commands into separate modules
* Create a reusable command-router class
* Add automated tests
* Package the command router as a reusable CLI framework

These improvements will be introduced progressively as the roadmap moves toward advanced tooling and application architecture.

## Development Philosophy

This repository follows:

```text
Learn
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Understand
  ↓
Repeat
```

The goal is not simply to make commands work, but to understand how command-line input can be parsed and dynamically mapped to reusable functions.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
