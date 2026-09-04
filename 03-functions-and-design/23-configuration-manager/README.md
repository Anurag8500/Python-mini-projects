# Project #23: Configuration Manager

A small Python-based configuration manager that demonstrates how applications can load, modify, validate, and persist settings using nested dictionaries and JSON files.

This project is part of **Phase 03 — Functions & Program Design** and introduces a practical combination of reusable functions, nested data, filesystem operations, JSON serialization, and configuration validation.

The project is intentionally kept small so the focus remains on understanding the underlying concepts.

## Features

* Load configuration from a JSON file
* Use default configuration when no file exists
* View the complete configuration
* Read individual settings
* Update existing settings
* Reset configuration to defaults
* Search settings
* Validate configuration values
* Save configuration changes
* Work with nested settings using dot notation

## Concepts Practiced

### Functions

* Function definitions
* Function calls
* Parameters
* Return values
* Helper functions
* Functions with specific responsibilities
* Functions calling other functions

### Configuration

* Default configuration
* Nested configuration
* Configuration lookup
* Configuration updates
* Configuration validation
* Persistent settings

### JSON

* `json.load()`
* `json.dump()`
* JSON serialization
* JSON deserialization
* Reading JSON files
* Writing JSON files

### Filesystem

* `pathlib.Path`
* `Path.exists()`
* `Path.open()`
* File reading
* File writing

### Data Structures

* Dictionaries
* Nested dictionaries
* Lists
* Tuples

### Error Handling

* `try / except`
* `OSError`
* `json.JSONDecodeError`
* Invalid configuration handling

## Why This Project Exists

Most earlier projects stored all data directly in Python variables.

For example:

```text
Python program
      ↓
Lists / dictionaries
      ↓
Program exits
      ↓
Data disappears
```

A configuration system is different.

The application can store its settings in a file:

```text
Python program
      ↓
config.json
```

The next time the program starts, it can load those settings again.

This introduces the concept of **persistent state**.

## Default Configuration

The application starts with a default configuration:

```python
default_config = {
    "app": {
        "name": "Python Toolkit",
        "debug": False
    },
    "user": {
        "username": "anurag",
        "theme": "dark"
    },
    "display": {
        "page_size": 20,
        "show_timestamps": True
    }
}
```

The configuration is represented using nested dictionaries.

Conceptually:

```text
config
├── app
│   ├── name
│   └── debug
├── user
│   ├── username
│   └── theme
└── display
    ├── page_size
    └── show_timestamps
```

## JSON Persistence

The configuration is stored in:

```text
config.json
```

When the program starts:

```python
json.load(file)
```

reads the JSON file and converts it into Python data.

When the configuration is saved:

```python
json.dump(
    config,
    file,
    indent=4
)
```

converts the Python dictionary into JSON.

The overall flow is:

```text
JSON file
   ↓
json.load()
   ↓
Python dictionary
   ↓
Application modifies settings
   ↓
json.dump()
   ↓
JSON file
```

## Configuration Paths

Nested settings can be referenced using dot notation.

Examples:

```text
app.name
app.debug
user.username
user.theme
display.page_size
```

For example:

```text
user.theme
```

represents:

```text
config
  ↓
user
  ↓
theme
```

The function:

```python
get_setting("user.theme")
```

walks through the nested dictionaries and returns:

```text
dark
```

## Getting Settings

The function:

```python
get_setting(path)
```

retrieves a setting using its dot-separated path.

Example:

```python
get_setting("app.name")
```

returns:

```text
Python Toolkit
```

The function returns `None` when the requested path does not exist.

## Setting Values

The function:

```python
set_setting(path, value)
```

updates an existing configuration value.

For example:

```text
user.theme
```

can be changed from:

```text
dark
```

to:

```text
light
```

The function walks through the nested dictionaries until it reaches the final key.

## Converting User Input

Terminal input always arrives as a string.

For example:

```text
20
```

initially arrives as:

```python
"20"
```

The `convert_value()` function converts simple values:

```text
"true"  → True
"false" → False
"20"    → 20
"hello" → "hello"
```

This allows configuration values to retain useful Python types instead of storing everything as strings.

## Configuration Validation

The function:

```python
validate_config()
```

checks whether important settings have valid values.

For example:

```text
app.name
```

must be text.

```text
app.debug
```

must be a Boolean.

```text
display.page_size
```

must be a positive integer.

```text
user.theme
```

must be either:

```text
dark
light
```

Validation errors are collected into a list and returned to the caller.

Example:

```text
Configuration errors:
- display.page_size must be greater than 0.
- user.theme must be dark or light.
```

## Resetting Configuration

The reset option replaces the current configuration with the default configuration.

This demonstrates the idea of maintaining a known baseline configuration.

After resetting:

```text
Modified configuration
        ↓
Default configuration
```

The reset happens in memory first. The user can then save it to `config.json`.

## Searching Settings

The search feature recursively walks through nested dictionaries and finds setting names containing a keyword.

For example, searching for:

```text
theme
```

can return:

```text
user.theme = dark
```

The recursive search demonstrates how a function can process nested data structures.

## Recursive Processing

The search function checks each value.

If the value is another dictionary:

```python
isinstance(value, dict)
```

the function calls itself again.

Conceptually:

```text
config
  ↓
app
  ↓
user
  ↓
display
```

The function keeps descending until it reaches non-dictionary values.

This is a first practical introduction to **recursion**.

## Main Menu

```text
=== Menu ===
1. View configuration
2. Get setting
3. Set setting
4. Reset configuration
5. Search setting
6. Validate configuration
7. Save configuration
8. Exit
```

## Example Workflow

A typical session can follow:

```text
Start program
      ↓
Load config.json
      ↓
View configuration
      ↓
Get a setting
      ↓
Change a setting
      ↓
Validate configuration
      ↓
Save configuration
      ↓
Exit
```

The next time the program starts, the saved configuration is loaded again.

## Project Structure

```text
23-configuration-manager/
│
├── main.py
├── README.md
└── config.json        # created after saving
```

`config.json` is generated by the program and stores the current configuration.

## How to Run

From the project directory:

```bash
python main.py
```

The application will use the default configuration if `config.json` does not exist.

Use the **Save configuration** option to create or update the JSON file.

## Important Design Pattern

This project continues the separation of responsibilities introduced in earlier projects:

```text
load_config()
     ↓
load data

get_setting()
     ↓
retrieve data

set_setting()
     ↓
modify data

validate_config()
     ↓
check data

save_config()
     ↓
persist data
```

Each function has a clear responsibility instead of one large block handling everything.

## Learning Progression

Project #23 combines several concepts developed recently:

```text
Project #18
Functions + modular design
        ↓
Project #19
Reusable validation functions
        ↓
Project #20
Function composition
        ↓
Project #21
Filesystem operations
        ↓
Project #22
Command routing
        ↓
Project #23
Configuration + JSON persistence
```

The key progression is:

```text
Functions
   ↓
Reusable functions
   ↓
Functions working with files
   ↓
Persistent application data
```

## Why This Project Matters

Configuration systems are used in almost every practical application.

Examples include:

```text
Application settings
Database configuration
API settings
Feature flags
Logging configuration
User preferences
Environment-specific settings
```

The important lesson is learning how to separate **application configuration from application code**.

Instead of hard-coding every setting inside the Python program, the application can read its settings from external data.

## Future Improvements

Possible extensions include:

* Support arbitrary nested settings
* Add and remove configuration keys
* Create a dedicated configuration module
* Support environment variables
* Add configuration schemas
* Add stronger type validation
* Support multiple configuration files
* Add development / production profiles
* Encrypt sensitive configuration values
* Add automated tests
* Package the configuration manager as a reusable library

These improvements will be introduced progressively as the roadmap moves toward tooling, testing, backend development, and production engineering.

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

The objective is to understand how configuration data moves between Python objects and persistent files, and how reusable functions can manage that process cleanly.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
