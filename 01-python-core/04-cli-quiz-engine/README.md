# CLI Quiz Engine

A command-line Python quiz application that presents multiple-choice questions, validates user input, tracks performance, and provides a final score with incorrect-answer review.

## Features

* Multiple-choice Python questions
* Randomized question order
* Interactive command-line interface
* Input validation for answer choices
* Case-insensitive answers
* Score tracking
* Correct and incorrect answer tracking
* Final percentage calculation
* Performance evaluation
* Review of incorrect answers
* Handles perfect scores separately

## Concepts Practiced

* Variables and data types
* Lists
* Dictionaries
* Nested data structures
* Lists containing dictionaries
* Loops
* Nested loops
* Conditional statements
* Boolean values
* String methods:

  * `.strip()`
  * `.upper()`
* Membership testing with `in`
* Dictionary access
* Dictionary methods
* `append()`
* `enumerate()`
* `len()`
* `while True`
* `break`
* `if` / `elif` / `else`
* Accumulator variables
* Basic calculations
* F-strings
* Number formatting with `:.2f`
* Importing and using modules
* `random.shuffle()`
* Basic input validation
* Collecting and processing results

## Data Structure

Questions are stored as a list of dictionaries.

Each question contains:

```python
{
    "question": "Which data structure stores key-value pairs?",
    "options": [
        "A. List",
        "B. Tuple",
        "C. Dictionary",
        "D. Set"
    ],
    "answer": "C"
}
```

Incorrect answers are stored separately for review:

```python
{
    "question": "...",
    "your_answer": "A",
    "correct_answer": "C"
}
```

## How It Works

```text
Create question data
        ↓
Shuffle questions
        ↓
Initialize score and wrong answers
        ↓
Display each question
        ↓
Display options
        ↓
Validate user input
        ↓
Check answer
        ↓
Update score or record mistake
        ↓
Calculate final statistics
        ↓
Display performance
        ↓
Review incorrect answers
```

## Example

```text
=== Python Quiz ===

Question 1/8
Which data structure stores key-value pairs?
A. List
B. Tuple
C. Dictionary
D. Set
Your answer: c
✓ Correct!

Question 2/8
Which operator is used for exponentiation in Python?
A. ^
B. **
C. //
D. %%
Your answer: A
✗ Incorrect. Correct answer: B

...

=== Final Result ===
Score: 6/8
Correct: 6
Incorrect: 2
Percentage: 75.00%
Performance: Good job!

=== Review Incorrect Answers ===

1. Which operator is used for exponentiation in Python?
   Your answer: A
   Correct answer: B
```

## What I Learned

* How to represent structured questions using dictionaries
* How to store multiple records in a list
* How nested data structures work
* How to shuffle a list using `random.shuffle()`
* How to validate user input before processing it
* How `while True` and `break` can create a validation loop
* How to normalize user input using `.strip()` and `.upper()`
* How to maintain a running score using an accumulator
* How to collect incorrect results for later analysis
* How to calculate percentages from collected results
* How `enumerate()` can provide both a position and an item
* How truthiness can be used to check whether a list contains data

## Possible Improvements

* Add question categories
* Add difficulty levels
* Show progress and current score during the quiz
* Hide the correct answer until the final review
* Track performance by category
* Track performance by difficulty
* Add a timer for each question
* Add multiple quiz modes
* Load questions from a JSON file
* Allow users to create their own question sets
* Refactor the program into reusable functions
* Add automated tests

## Project Structure

```text
04-cli-quiz-engine/
│
├── main.py
└── README.md
```

## Status

**Completed — Phase 01: Python Core**

Project 04 of the Python Mini Projects curriculum.
