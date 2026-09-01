# Contact Management System

A command-line Python application for managing a collection of contacts. The system supports creating, viewing, searching, updating, deleting, filtering, and sorting contacts while enforcing basic data validation and uniqueness rules.

This project begins **Phase 02 — Data & Logic** of the Python Mini Projects curriculum and focuses on reasoning about structured collections of real-world data.

## Features

* View all contacts
* Add new contacts
* Assign unique contact IDs
* Store:

  * Name
  * Phone number
  * Email address
  * Category
* Prevent duplicate phone numbers
* Search contacts by:

  * Name
  * Phone number
  * Email
* Update existing contact information
* Prevent duplicate phone numbers during updates
* Delete contacts
* Filter contacts by category
* Sort contacts by:

  * Name
  * Category
  * ID
* Display contact statistics
* Validate user input
* Handle invalid contact IDs
* Normalize text input for consistent searching and storage

## Concepts Practiced

* Variables and data types
* Strings and string methods
* `.strip()`
* `.lower()`
* `.upper()`
* `.title()`
* Lists
* Dictionaries
* Lists of dictionaries
* Nested data structures
* Dictionary access and updates
* Dictionary `.items()`
* Dictionary membership with `in`
* `append()`
* `remove()`
* `len()`
* `sorted()`
* `key=`
* `lambda`
* `while True`
* `for` loops
* `if / elif / else`
* `break`
* `continue`
* `try / except`
* `ValueError`
* Boolean values
* Flag variables
* List comprehensions
* Membership testing
* Searching
* Filtering
* Sorting
* Aggregation
* Frequency counting
* Compound conditions using `and` / `or`
* Unique identifiers
* Data validation
* Data integrity
* Application state management

## Data Structure

Each contact is represented using a dictionary:

```python id="9c9r4p"
{
    "id": 1,
    "name": "Anurag Bardhan",
    "phone": "9876543210",
    "email": "anurag@example.com",
    "category": "friend"
}
```

Multiple contacts are stored in a list:

```python id="yq5ss7"
contacts = [
    {
        "id": 1,
        "name": "Anurag Bardhan",
        "phone": "9876543210",
        "email": "anurag@example.com",
        "category": "friend"
    },
    {
        "id": 2,
        "name": "Rahul Sharma",
        "phone": "9123456780",
        "email": "rahul@example.com",
        "category": "work"
    }
]
```

A separate counter is used to generate stable contact IDs:

```python id="0m0xpy"
next_contact_id = 4
```

The contact's ID remains independent of its position in the list.

## CRUD Operations

The system implements the four fundamental data-management operations:

```text id="tp7v3y"
Create
  ↓
Add a contact

Read
  ↓
View, search, filter, and sort contacts

Update
  ↓
Modify contact information

Delete
  ↓
Remove a contact
```

These concepts will later be reused with files, databases, and APIs.

## Search

The search system checks multiple contact fields.

A search term can match:

```text id="4cjy5h"
Name
Phone
Email
```

For example, searching for:

```text id="pl3eim"
anurag
```

can match a contact's name, while:

```text id="t3cok0"
9876
```

can match a phone number.

Search is case-insensitive for text fields.

## Filtering

Contacts can be filtered by category:

```text id="g8i93u"
friend
family
work
other
```

The original `contacts` list remains unchanged while a temporary filtered list is created.

## Sorting

The application can sort contacts by:

* Name
* Category
* ID

Sorting is performed using `sorted()` with a `key` function.

For example:

```python id="7e4wbh"
sorted(
    contacts,
    key=lambda contact: contact["name"].lower()
)
```

This creates a new sorted list without changing the original contact order.

## Data Validation and Integrity

The application applies several basic rules:

* Name cannot be empty
* Phone number cannot be empty
* Email cannot be empty
* Phone numbers must be unique
* Invalid categories are rejected
* Invalid contact IDs are handled
* User input is normalized before processing

When updating a contact, its existing phone number is allowed to remain unchanged, but a phone number belonging to a different contact cannot be reused.

## Normalized Input

Text input is normalized before storage or searching.

For example:

```text id="aucdm2"
FRIEND
Friend
friend
 friend
```

can be normalized to:

```text id="2uo3b9"
friend
```

The value can then be formatted using `.title()` when displayed.

This separates **internal data representation** from **display formatting**.

## How It Works

```text id="n5q2qe"
Start application
       ↓
Load contact data
       ↓
Display menu
       ↓
Choose operation
       ↓
Validate input
       ↓
Search / add / update / delete / filter / sort
       ↓
Modify or retrieve contact data
       ↓
Display result
       ↓
Return to menu
       ↓
Exit
```

## Example

```text id="4t7o6r"
=== Contact Management System ===

=== Menu ===
1. View contacts
2. Add contact
3. Search contacts
4. Update contact
5. Delete contact
6. Filter contacts
7. Sort contacts
8. Show statistics
9. Exit

Choose an option: 2

Name: john doe
Phone: 9999999999
Email: JOHN@EXAMPLE.COM
Category: WORK

Contact #4 added successfully.
```

Viewing contacts:

```text id="x6hzi6"
=== Contacts ===
[1] Anurag Bardhan | 9876543210 | anurag@example.com | Friend
[2] Rahul Sharma | 9123456780 | rahul@example.com | Work
[3] Priya Singh | 9988776655 | priya@example.com | Family
[4] John Doe | 9999999999 | john@example.com | Work
```

Search example:

```text id="ba3myc"
Search by name, phone, or email: example.com

=== Search Results ===
[1] Anurag Bardhan | 9876543210 | anurag@example.com | Friend
[2] Rahul Sharma | 9123456780 | rahul@example.com | Work
[3] Priya Singh | 9988776655 | priya@example.com | Family
[4] John Doe | 9999999999 | john@example.com | Work
```

Statistics:

```text id="z4y4yy"
=== Contact Statistics ===
Total contacts: 4

By category:
- Friends: 1
- Family: 1
- Work: 2
- Other: 0
```

## What I Learned

* How to model real-world records using dictionaries
* How to manage multiple records using lists
* How stable IDs can identify records independently of list positions
* How to search across multiple fields
* How to create filtered subsets of structured data
* How `sorted()` and `key=` can order records by different attributes
* How compound conditions using `and` and `or` can express more complex rules
* How flag variables can track whether a record was found
* How duplicate detection can protect data integrity
* How to update an existing dictionary stored inside a list
* How temporary result lists can be created for searching and filtering
* How previously learned frequency-counting patterns can be reused for statistics
* How to normalize data before storing and comparing it

## Limitations

* Contacts are stored only in memory
* Data is lost when the program exits
* The application is currently implemented in a single Python file
* Phone and email validation is intentionally basic
* No automated tests are included

These limitations are intentional at this stage of the curriculum.

Persistent storage, stronger validation, modular architecture, and testing will be introduced later.

## Possible Improvements

* Validate phone number format
* Validate email format
* Search by category
* Sort in ascending or descending order
* Add email duplicate detection
* Add contact notes
* Add multiple phone numbers
* Add contact timestamps
* Import contacts from CSV or JSON
* Export contacts to CSV or JSON
* Persist contacts using SQLite
* Refactor the program into reusable functions
* Separate the application into modules
* Add automated tests

## Project Structure

```text id="rp2qgr"
09-contact-management-system/
│
├── main.py
└── README.md
```

## Phase Progress

This project begins:

**Phase 02 — Data & Logic**

Previous phase completed:

**Phase 01 — Python Core**

Current project:

**Project 09 — Contact Management System**

## Status

**Completed — Phase 02: Data & Logic**
