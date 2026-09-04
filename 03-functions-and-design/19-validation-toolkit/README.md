# Project #19: Validation Toolkit

A Python-based validation toolkit containing reusable functions for validating common types of user input.

This project is part of **Phase 03 — Functions & Program Design** and focuses on designing small, reusable functions with clear responsibilities and predictable return values.

Instead of embedding validation logic directly inside a program's main workflow, the project separates validation into independent functions that return `True` or `False`.

## Features

* Validate email addresses
* Validate phone numbers
* Validate passwords
* Validate usernames
* Validate ages
* Validate numerical ranges
* Validate choices against allowed values
* Validate dates
* Validate names
* Validate complete user data
* Display validation results
* Reuse validation functions across multiple workflows

## Concepts Practiced

### Functions

* Function definitions
* Function calls
* Parameters
* Arguments
* Return values
* Boolean-returning functions
* Default parameters
* Function composition
* Reusable helper functions
* Single-responsibility functions

### Data Processing

* Strings
* Lists
* Dictionaries
* Dictionary `.items()`
* Dictionary `.values()`
* `len()`
* `sum()`
* `split()`
* `join()`
* String methods
* Conditional logic

### Validation

* Empty input validation
* Length validation
* Character validation
* Numeric range validation
* Format validation
* Multiple-condition validation
* Leap-year validation

### Control Flow

* `if / elif / else`
* `for` loops
* `while` loops
* `break`
* `continue`
* `try / except`

## Why This Project Exists

Before this project, validation logic was repeatedly written directly inside application code.

Examples included:

```python
if not name:
    ...
```

```python
if amount <= 0:
    ...
```

```python
if category not in valid_categories:
    ...
```

and:

```python
try:
    value = int(...)
except ValueError:
    ...
```

Repeating these checks makes larger programs harder to maintain.

Project #19 moves this logic into reusable functions.

Instead of:

```text
Application
    ↓
Validation logic everywhere
```

the structure becomes:

```text
Application
    ↓
Validation function
    ↓
True / False
```

## Main Menu

```text
=== Menu ===
1. Validate email
2. Validate phone number
3. Validate password
4. Validate username
5. Validate age
6. Validate number range
7. Validate choice
8. Validate date
9. Validate name
10. Validate complete user data
11. Exit
```

## Email Validation

The email validator checks for a basic email structure.

Example:

```python
is_valid_email("user@example.com")
```

returns:

```python
True
```

while clearly malformed values return:

```python
False
```

The function checks conditions such as:

* Non-empty value
* No spaces
* Exactly one `@`
* Non-empty username
* Non-empty domain
* Domain contains `.`
* Domain does not start or end with `.`

The validator intentionally performs **basic structural validation** rather than attempting to implement the complete email specification.

## Phone Validation

The phone validator checks for:

* Exactly 10 digits
* No letters
* No spaces
* No additional characters

Example:

```python
is_valid_phone("9876543210")
```

returns:

```python
True
```

while:

```python
is_valid_phone("98765abc10")
```

returns:

```python
False
```

## Password Validation

The password validator requires:

* At least 8 characters
* At least one uppercase character
* At least one lowercase character
* At least one digit

For example:

```text
Python123
```

satisfies the basic rules.

The function tracks the required character types while iterating through the password.

This introduces the idea of maintaining multiple boolean flags during validation.

## Username Validation

The username validator requires:

* 3–20 characters
* First character must be a letter
* Remaining characters may contain letters
* Numbers are allowed
* Underscores are allowed
* Other special characters are rejected

Example:

```text
anurag_123
```

is valid.

A username such as:

```text
123anurag
```

is rejected because it starts with a number.

## Age Validation

The age validator uses default parameters:

```python
def is_valid_age(age, minimum=1, maximum=120):
```

This means the function can normally be called as:

```python
is_valid_age(25)
```

while still allowing a custom range:

```python
is_valid_age(25, 18, 60)
```

The function returns `True` when the age falls within the inclusive range.

## Number Range Validation

The generic number validator accepts a value and a valid range:

```python
is_valid_number(
    value,
    minimum,
    maximum
)
```

The core condition is:

```python
minimum <= value <= maximum
```

This makes the function reusable for many different types of numeric validation.

Examples include:

```text
Age
Marks
Price
Rating
Percentage
Quantity
```

## Choice Validation

The choice validator checks whether a value exists in a collection of accepted values.

Example:

```python
valid_choices = [
    "yes",
    "no",
    "maybe"
]
```

Then:

```python
is_valid_choice(
    "yes",
    valid_choices
)
```

returns:

```python
True
```

while an unsupported choice returns `False`.

This is a simple but highly reusable validation pattern.

## Date Validation

The date validator accepts dates in:

```text
YYYY-MM-DD
```

format.

For example:

```text
2026-09-04
```

The function checks:

* Correct number of components
* Numeric year, month, and day
* Valid month range
* Valid day range
* February leap-year rules

Leap years are handled using the standard rule:

```text
Divisible by 400
OR
Divisible by 4 but not by 100
```

This prevents invalid dates such as:

```text
2026-02-30
```

from being accepted.

## Name Validation

The name validator allows:

* Alphabetic characters
* Spaces

It rejects empty values and characters that do not belong in a basic name field.

For example:

```text
Anurag Bardhan
```

is valid.

## Complete User Validation

The project also demonstrates how small validation functions can be combined.

The program collects:

```text
Name
Username
Email
Phone
Age
Password
Date
```

and sends them to:

```python
validate_user_data(...)
```

That function returns a dictionary:

```python
{
    "name": True,
    "username": True,
    "email": True,
    "phone": True,
    "age": True,
    "password": False,
    "date": True
}
```

This provides a structured overview of the validation results.

## Boolean Return Values

One of the most important design decisions in this project is that validation functions return a boolean.

For example:

```python
def is_valid_age(age):
    if age < 1:
        return False

    if age > 120:
        return False

    return True
```

The function does not print:

```text
Age is valid
```

Instead, it returns:

```text
True
```

or:

```text
False
```

The caller decides what should happen next.

This makes the function reusable in many environments, including programs that do not have a terminal interface.

## Separation of Responsibilities

The project separates validation from presentation.

For example:

```text
is_valid_email()
        ↓
validation
        ↓
True / False
        ↓
display_validation_result()
        ↓
terminal output
```

This is different from putting validation and printing inside the same function.

The separation makes the validation logic easier to reuse and eventually test independently.

## Helper Functions

The project includes small helper functions such as:

```python
find
calculate
validate
display
```

Each function is designed around a specific responsibility.

Examples:

```text
is_valid_email()
    → Validate email structure

is_valid_phone()
    → Validate phone format

is_valid_age()
    → Validate age range

display_validation_result()
    → Display a validation result
```

This is an introduction to the idea of **single responsibility**.

## Project Structure

```text
19-validation-toolkit/
│
├── main.py
└── README.md
```

The toolkit remains in a single file for now.

Later projects will begin separating reusable functionality into dedicated modules and packages.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure your Python virtual environment is activated before running the program.

## Example Workflow

A typical session might look like:

```text
Choose an option: 1

=== Email Validation ===
Enter email: user@example.com
✓ Email: Valid
```

Another example:

```text
Choose an option: 3

=== Password Validation ===
Enter password: hello123
✗ Password: Invalid
```

And complete validation:

```text
Choose an option: 10

=== Complete User Validation ===

Name: Anurag Bardhan
Username: anurag_123
Email: anurag@example.com
Phone: 9876543210
Age: 21
Password: Python123
Date: 2026-09-04

=== Validation Results ===
✓ Name: Valid
✓ Username: Valid
✓ Email: Valid
✓ Phone: Valid
✓ Age: Valid
✓ Password: Valid
✓ Date: Valid

Valid fields: 7/7
All user data is valid.
```

## Function Design Pattern

The general pattern introduced in this project is:

```text
Input
  ↓
Function
  ↓
Validation / Processing
  ↓
Return value
```

For example:

```python
result = is_valid_email(email)
```

The calling code can then decide how to use `result`.

This pattern is more flexible than having the validation function directly control the program's output.

## Why This Project Matters

Validation appears almost everywhere in software:

```text
Forms
APIs
Databases
Authentication
Payments
CLI applications
Web applications
Configuration systems
```

Building small reusable validators now makes later projects easier to structure.

The larger lesson is not just how to validate an email or password. It is learning how to take a repeated piece of logic and turn it into a **reusable function with a clear input and output contract**.

## Learning Progression

Project #19 builds directly on Project #18:

```text
Project #18
Modular Expense Tracker
        ↓
Functions + parameters + return values
        ↓
Project #19
Reusable validation functions
        ↓
Small functions with clear responsibilities
        ↓
Future projects
Reusable tools + modules + packages
```

The focus is gradually shifting from simply writing programs to designing reusable components.

## Future Improvements

Possible extensions include:

* Return detailed validation error messages
* Create reusable input-prompt functions
* Support international phone formats
* Improve email validation
* Support more username rules
* Add password strength levels
* Validate URLs
* Validate file paths
* Validate hexadecimal colors
* Validate JSON strings
* Validate IP addresses
* Move validators into a separate module
* Add unit tests
* Package the toolkit for reuse in other projects

These improvements will be introduced progressively as the roadmap moves toward modular packages, testing, and production-quality Python applications.

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

The goal is not simply to make the validation work, but to understand how small functions can be designed, composed, reused, and eventually tested independently.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
