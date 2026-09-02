# Project #14: Event Registration Manager

A Python-based terminal application for creating events, registering participants, managing registrations, and analyzing event capacity and attendance.

This project introduces a more relational data structure where **events contain collections of participant records**. It combines CRUD operations, nested data, validation, searching, filtering, aggregation, and occupancy analysis into one interactive application.

## Features

* View all events
* Create new events
* Register participants for events
* Prevent duplicate participant registrations
* Prevent registrations when an event is full
* Cancel participant registrations
* View participants for a specific event
* Search events by name or category
* Filter events by category
* Filter events with available seats
* Filter full events
* Calculate event statistics
* Analyze registration statistics by category
* Calculate event occupancy rates
* Generate a detailed event report
* Maintain unique event and participant IDs

## Concepts Practiced

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Nested dictionaries
* Lists stored inside dictionaries
* Dictionary `.get()`
* Dictionary `.items()`

### Control Flow

* `while` loops
* `for` loops
* Nested loops
* `if / elif / else`
* `break`
* `continue`

### Data Processing

* `len()`
* `sum()`
* `max()`
* `sorted()`
* `enumerate()`
* List comprehensions
* Generator expressions
* List slicing
* Aggregation
* Ranking

### Input Validation

* Empty input validation
* Numeric input validation
* Capacity validation
* Event ID validation
* Participant ID validation
* Duplicate event detection
* Duplicate participant detection
* Capacity validation

### String Processing

* `.strip()`
* `.lower()`
* `.title()`

## Data Structure

Each event is represented as a dictionary:

```python id="3y8t0j"
{
    "id": 1,
    "name": "Python Workshop",
    "category": "technical",
    "capacity": 50,
    "date": "15 September 2026",
    "participants": [
        {
            "id": 1,
            "name": "Anurag Bardhan",
            "email": "anurag@example.com"
        }
    ]
}
```

All events are stored inside a list:

```python id="36gl6g"
events = [
    {...},
    {...},
    {...}
]
```

The important part is the nested `participants` list.

This produces the following structure:

```text id="4j8k5j"
events
   ↓
event
   ↓
participants
   ├── participant
   ├── participant
   └── participant
```

This is a more complex data relationship than the flat records used in many earlier projects.

## Event Categories

The application supports:

```text id="2j6k7o"
Technical
Business
Creative
Sports
Education
Other
```

Events can later be filtered and analyzed based on these categories.

## Main Menu

```text id="j92p7t"
=== Menu ===
1. View all events
2. Create event
3. Register participant
4. Cancel registration
5. View event participants
6. Search events
7. Filter events
8. Event statistics
9. Registration statistics
10. Detailed report
11. Exit
```

## Event Management

### Create Event

A new event requires:

* Event name
* Category
* Date
* Capacity

The program validates the capacity and ensures that an event with the same name does not already exist.

Example:

```text id="3h6h6w"
=== Create Event ===

Event name: Python Bootcamp
Category: technical
Event date: 30 September 2026
Capacity: 40

Event created successfully with ID 4.
```

Each event starts with an empty participant list:

```python id="0fzz6j"
"participants": []
```

## Participant Registration

Participants can be registered for a specific event using its ID.

The program checks:

1. Whether the event exists
2. Whether seats are available
3. Whether the participant has already registered
4. Whether the participant's required information is valid

Example:

```text id="u0fda3"
Event: Python Workshop
Available seats: 48

Participant name: Sneha Roy
Participant email: sneha@example.com

Participant registered successfully with ID 5.
```

## Capacity Management

One of the main pieces of logic in this project is capacity management.

The number of registered participants is:

```python id="df5o8n"
len(event["participants"])
```

Available seats are calculated as:

```python id="gr38vs"
event["capacity"] - len(event["participants"])
```

For example:

```text id="8p9td4"
Capacity: 50
Registered: 42

Available seats = 50 - 42
                = 8
```

Registration is rejected once:

```python id="fz4goz"
len(event["participants"]) >= event["capacity"]
```

This prevents the event from exceeding its defined capacity.

## Duplicate Registration Prevention

A participant cannot register twice for the same event using the same email address.

The program checks each existing participant:

```python id="52c6v6"
for participant in selected_event["participants"]:
    if participant["email"] == email:
        ...
```

This demonstrates searching through a nested collection and validating a relationship between records.

## Cancel Registration

A registration can be cancelled by selecting:

* Event ID
* Participant ID

The participant is located inside that event's participant list and removed:

```python id="w67p8t"
selected_event["participants"].remove(
    selected_participant
)
```

This increases the number of available seats automatically because the participant is no longer part of the collection.

## Viewing Participants

The program can display all participants for a specific event.

Example:

```text id="x7shq3"
=== Participants: Python Workshop ===

1. Anurag Bardhan | anurag@example.com
2. Rahul Sharma | rahul@example.com
3. Sneha Roy | sneha@example.com

Registered: 3
Capacity: 50
Available seats: 47
```

This demonstrates traversal of nested lists and dictionaries.

## Searching Events

Events can be searched by:

* Event name
* Category

The search is case-insensitive.

For example:

```text id="2fmjqs"
python
```

can match:

```text id="qjp5mb"
Python Workshop
```

The search uses normalized text:

```python id="8vtmd0"
search_term = input(...).strip().lower()
```

and checks the event fields using:

```python id="y4ckw7"
search_term in event["name"].lower()
```

or:

```python id="1d3ujq"
search_term in event["category"].lower()
```

## Filtering Events

The program provides three types of filtering.

### Filter by Category

Displays only events belonging to a selected category.

### Events with Available Seats

Uses:

```python id="c3egpz"
len(event["participants"]) < event["capacity"]
```

to identify events that are not full.

### Full Events

Uses:

```python id="9uh1ha"
len(event["participants"]) >= event["capacity"]
```

to identify events that have reached their capacity.

This reinforces the filtering patterns used in previous projects.

## Event Statistics

The event statistics section calculates:

* Total number of events
* Total event capacity
* Total registrations
* Total available seats
* Most popular event
* Largest event

Example:

```text id="l6zh1s"
=== Event Statistics ===

Total events: 3
Total capacity: 100
Total registrations: 4
Available seats: 96
Most popular event: Python Workshop (2 registrations)
Largest event: Python Workshop (50 seats)
```

The most popular event is determined with:

```python id="9ti3ha"
most_popular_event = max(
    events,
    key=lambda event:
        len(event["participants"])
)
```

## Registration Statistics

The program groups events by category and calculates:

* Number of events
* Total registrations
* Total capacity
* Category fill rate

The category structure looks conceptually like:

```python id="yspq5h"
{
    "technical": {
        "event_count": 2,
        "registrations": 12,
        "capacity": 80
    }
}
```

The fill rate is calculated as:

```python id="qu4oek"
registrations / capacity * 100
```

For example:

```text id="h8zo8a"
Registrations: 30
Capacity: 50

Fill rate = 30 / 50 × 100
          = 60%
```

This provides a better measure of event performance than registration count alone.

## Event Occupancy Ranking

The detailed report ranks events by occupancy percentage rather than raw registration count.

The calculation is:

```python id="tk10a5"
len(event["participants"]) / event["capacity"]
```

For example:

```text id="zx5k0k"
Event A → 20 / 50 → 40%
Event B → 18 / 20 → 90%
```

Even though Event A has more registrations, Event B has the higher occupancy.

The program therefore ranks Event B higher.

This introduces the idea of ranking records using a **derived metric**.

## Detailed Report

The detailed report combines the main event-level statistics into one summary.

It includes:

### Overall Statistics

* Total events
* Total capacity
* Total registrations
* Available seats
* Average registrations per event
* Most popular event

### Category Statistics

* Number of events in each category

### Occupancy Ranking

* Event ranking
* Registered participants
* Capacity
* Occupancy percentage

Example:

```text id="m7yk6d"
========================================
       DETAILED EVENT REPORT
========================================

Total events          : 3
Total capacity       : 100
Total registrations   : 4
Available seats       : 96
Average registrations: 1.33

Most popular event   : Python Workshop

Events by category:
- Business: 1
- Creative: 1
- Technical: 1

Event occupancy:
1. Python Workshop — 2/50 (4.00%)
2. Startup Meetup — 1/30 (3.33%)
3. Photography Walk — 1/20 (5.00%)
```

## Derived Metrics

The program intentionally calculates information from the stored data rather than duplicating it inside the event record.

For example, available seats are derived from:

```text id="54cyg5"
Capacity - Registered Participants
```

Occupancy is derived from:

```text id="d4yjad"
Registered Participants / Capacity × 100
```

This means statistics automatically reflect changes whenever participants are registered or removed.

## Why This Project Matters

This project introduces an important step in program design:

**data relationships.**

Earlier projects primarily worked with one record at a time:

```text id="gk0ezm"
Student → Marks
Product → Stock
Expense → Category
```

This project introduces:

```text id="x5kgae"
Event
  ↓
Participants
```

One event can contain many participant records.

That relationship is a foundation for more advanced systems such as booking platforms, learning management systems, e-commerce applications, and database-backed applications.

## Project Structure

```text id="cbbm1f"
14-event-registration-manager/
│
├── main.py
└── README.md
```

The application intentionally remains a single-file program at this stage of the roadmap.

Functions and modular design will be introduced in the next phase to eliminate repeated logic and make larger programs easier to maintain.

## How to Run

From the project directory:

```bash id="lpf9l9"
python main.py
```

Make sure your Python virtual environment is activated before running the program.

## Example Workflow

```text id="x9nqqn"
Create an event
      ↓
Register participants
      ↓
View registrations
      ↓
Search / filter events
      ↓
Cancel registrations when necessary
      ↓
Analyze event statistics
      ↓
Analyze occupancy
      ↓
Generate detailed report
```

## Learning Progression

Project #14 builds on patterns introduced throughout the previous projects:

```text id="k1z1yw"
Project #09
CRUD + search + filtering
        ↓
Project #10
Sorting + aggregation
        ↓
Project #11
Grouping + statistics
        ↓
Project #13
Nested records + student analytics
        ↓
Project #14
Nested collections + relationships + capacity logic
```

The goal is to keep reusing familiar Python concepts while increasing the complexity of the data and the business rules.

## Future Improvements

Possible extensions include:

* Update event details
* Edit participant information
* Move participants between events
* Event date validation
* Waitlists for full events
* Multiple registration types
* Registration timestamps
* Event cancellation
* Import/export using CSV or JSON
* Persistent storage using a database
* Automated tests
* Refactoring into reusable functions and modules

These improvements are intentionally reserved for later stages of the roadmap.

## Development Philosophy

This repository follows:

```text id="tdq2gi"
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

The objective is to understand the logic behind every project rather than simply producing working code.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
